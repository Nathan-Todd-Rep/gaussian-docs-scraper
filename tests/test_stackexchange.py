from __future__ import annotations

import requests
from types import SimpleNamespace

from gaussian_scraper import stackexchange
from gaussian_scraper.stackexchange import discover_se_tags, fetch_se_passages


def _fake_response(status_code: int, data: dict):
    return SimpleNamespace(
        status_code=status_code,
        json=lambda: data,
    )


def _make_fake_get(questions_data: dict, answers_data: dict | None = None):
    """
    Returns a fake requests.get that dispatches by URL.
    Questions endpoint gets questions_data, answers endpoint gets answers_data.
    """
    answers_data = answers_data or {"items": []}

    def fake_get(url, *args, **kwargs):
        if "answers" in url:
            return _fake_response(200, answers_data)
        return _fake_response(200, questions_data)

    return fake_get


SAMPLE_QUESTION = {
    "question_id": 1,
    "title": "How do I set %mem and %nproc in Gaussian 16 for a Slurm job?",
    "body": "<p>I am trying to run a Gaussian g16 DFT calculation on an HPC cluster.</p>"
            "<p>What values should I use for %mem and %nproc in my input file?</p>",
    "score": 42,
}

SAMPLE_ANSWER = {
    "answer_id": 101,
    "question_id": 1,
    "body": "<p>Set %mem=8GB and %nproc=4 in your Gaussian input file to match your Slurm request.</p>",
    "score": 30,
    "is_accepted": True,
}


# --- failure cases ---

def test_fetch_se_returns_none_on_request_error(monkeypatch):
    def fake_get(*args, **kwargs):
        raise requests.RequestException("connection refused")

    monkeypatch.setattr(requests, "get", fake_get)

    result = fetch_se_passages(tag="gaussian", site="chemistry")

    assert result is None


def test_fetch_se_returns_none_on_non_200(monkeypatch):
    monkeypatch.setattr(
        requests,
        "get",
        lambda *a, **kw: _fake_response(403, {}),
    )

    result = fetch_se_passages(tag="gaussian", site="chemistry")

    assert result is None


def test_fetch_se_returns_none_when_no_items(monkeypatch):
    monkeypatch.setattr(
        requests,
        "get",
        _make_fake_get({"items": [], "has_more": False}),
    )

    result = fetch_se_passages(tag="gaussian", site="chemistry")

    assert result is None


# --- question passage extraction ---

def test_fetch_se_extracts_title_as_passage(monkeypatch):
    monkeypatch.setattr(
        requests,
        "get",
        _make_fake_get({"items": [SAMPLE_QUESTION]}),
    )

    result = fetch_se_passages(tag="gaussian", site="chemistry")

    assert result is not None
    assert any("%mem" in p for p in result)


def test_fetch_se_strips_html_from_body(monkeypatch):
    question = {
        "question_id": 2,
        "title": "Gaussian 16 memory settings for DFT calculations on HPC.",
        "body": "<p>Use <strong>%mem=8GB</strong> and <code>%nproc=4</code> in your Gaussian input file.</p>",
        "score": 5,
    }

    monkeypatch.setattr(
        requests,
        "get",
        _make_fake_get({"items": [question]}),
    )

    result = fetch_se_passages(tag="gaussian", site="chemistry")

    assert result is not None
    assert all("<" not in p for p in result)
    assert any("%mem" in p or "Gaussian" in p for p in result)


def test_fetch_se_body_splits_into_separate_paragraph_passages(monkeypatch):
    question = {
        "question_id": 3,
        "title": "Short title",
        "body": (
            "<p>Use %mem=8GB and %nproc=4 in your Gaussian input file for the job.</p>"
            "<p>Also remember to load the gaussian module before submitting via slurm.</p>"
        ),
        "score": 1,
    }

    monkeypatch.setattr(
        requests,
        "get",
        _make_fake_get({"items": [question]}),
    )

    result = fetch_se_passages(
        tag="gaussian", site="chemistry",
        keywords=["gaussian", "%mem", "%nproc", "slurm"],
    )

    assert result is not None
    # The two <p> tags should become two distinct passages, not one
    # giant blob with both sentences merged together.
    assert any(p.startswith("Use %mem=8GB") and "Also remember" not in p for p in result)
    assert any(p.startswith("Also remember") for p in result)


def test_fetch_se_caps_at_max_passages(monkeypatch):
    monkeypatch.setattr(stackexchange, "MAX_PASSAGES_PER_SOURCE", 3)

    items = [
        {
            "question_id": i,
            "title": f"How do I use Gaussian g16 with DFT for calculation number {i}?",
            "body": f"<p>Use Gaussian g16 with %mem=8GB and %nproc=4 for job {i} on the cluster.</p>",
            "score": 10 - i,
        }
        for i in range(10)
    ]

    monkeypatch.setattr(
        requests,
        "get",
        _make_fake_get({"items": items}),
    )

    result = fetch_se_passages(tag="gaussian", site="chemistry")

    assert result is not None
    assert len(result) == 3


# --- scoring / prioritization ---

def test_fetch_se_prioritizes_higher_scoring_passages_when_over_cap(monkeypatch):
    monkeypatch.setattr(stackexchange, "MAX_PASSAGES_PER_SOURCE", 1)

    weak_line = "Gaussian is mentioned here once and nothing else relevant at all."
    strong_line = "Use Gaussian with slurm sbatch and %mem settings for the job today."

    question = {
        "question_id": 1,
        "title": "Short title",
        # weak line appears first in the body -- under the old first-match
        # behavior it would have won the single cap slot.
        "body": f"<p>{weak_line}</p><p>{strong_line}</p>",
        "score": 10,
    }

    monkeypatch.setattr(
        requests,
        "get",
        _make_fake_get({"items": [question]}),
    )

    result = fetch_se_passages(
        tag="gaussian", site="chemistry",
        keywords=["gaussian", "slurm", "sbatch", "%mem"],
    )

    assert result == [strong_line]


def test_fetch_se_always_fetches_answers_even_when_cap_already_met(monkeypatch):
    monkeypatch.setattr(stackexchange, "MAX_PASSAGES_PER_SOURCE", 1)

    question = {
        "question_id": 1,
        "title": "How do I use Gaussian g16 for a calculation on the cluster today?",
        "body": "<p>Some unrelated body text that still mentions gaussian once here.</p>",
        "score": 10,
    }
    # The answer is more keyword-dense than the question title, so it
    # should win the single cap slot -- but only if it was actually fetched.
    answer = {
        "answer_id": 100,
        "question_id": 1,
        "body": "<p>Use Gaussian g16 with slurm sbatch and %mem plus %nproc settings.</p>",
        "score": 5,
    }

    monkeypatch.setattr(
        requests,
        "get",
        _make_fake_get(
            questions_data={"items": [question]},
            answers_data={"items": [answer]},
        ),
    )

    result = fetch_se_passages(
        tag="gaussian", site="chemistry",
        keywords=["gaussian", "slurm", "sbatch", "%mem", "%nproc"],
    )

    assert result is not None
    assert "slurm sbatch and %mem plus %nproc" in result[0]


# --- deduplication ---

def test_fetch_se_deduplicates_repeated_lines(monkeypatch):
    duplicated_line = "Use Gaussian g16 with %mem=8GB and %nproc=4 on the cluster for this job."
    questions = [
        {
            "question_id": 1,
            "title": "Short title one",
            "body": f"<p>{duplicated_line}</p>",
            "score": 10,
        },
        {
            "question_id": 2,
            "title": "Short title two",
            "body": f"<p>{duplicated_line}</p>",
            "score": 9,
        },
    ]

    monkeypatch.setattr(
        requests,
        "get",
        _make_fake_get({"items": questions}),
    )

    result = fetch_se_passages(tag="gaussian", site="chemistry")

    assert result is not None
    assert result.count(duplicated_line) == 1


# --- answer passage extraction ---

def test_fetch_se_includes_answer_passages(monkeypatch):
    question_with_no_body = {
        "question_id": 1,
        "title": "Short title",
        "body": "<p>Short.</p>",
        "score": 10,
    }

    monkeypatch.setattr(
        requests,
        "get",
        _make_fake_get(
            questions_data={"items": [question_with_no_body]},
            answers_data={"items": [SAMPLE_ANSWER]},
        ),
    )

    result = fetch_se_passages(tag="gaussian", site="chemistry")

    assert result is not None
    assert any("%mem" in p for p in result)


def test_fetch_se_answer_html_is_stripped(monkeypatch):
    answer_with_html = {
        "answer_id": 200,
        "question_id": 1,
        "body": "<p>Use <code>%mem=16GB</code> and <strong>%nproc=8</strong> for large Gaussian DFT jobs on the cluster.</p>",
        "score": 20,
    }

    monkeypatch.setattr(
        requests,
        "get",
        _make_fake_get(
            questions_data={"items": [SAMPLE_QUESTION]},
            answers_data={"items": [answer_with_html]},
        ),
    )

    result = fetch_se_passages(tag="gaussian", site="chemistry")

    assert result is not None
    assert all("<" not in p for p in result)


def test_fetch_se_returns_question_passages_if_answers_fail(monkeypatch):
    def fake_get(url, *args, **kwargs):
        if "answers" in url:
            raise requests.RequestException("timeout")
        return _fake_response(200, {"items": [SAMPLE_QUESTION]})

    monkeypatch.setattr(requests, "get", fake_get)

    result = fetch_se_passages(tag="gaussian", site="chemistry")

    assert result is not None
    assert len(result) > 0


# --- discover_se_tags ---

def test_discover_returns_empty_for_empty_topic(monkeypatch):
    called = []

    def fake_get(*args, **kwargs):
        called.append(True)
        return _fake_response(200, {"items": []})

    monkeypatch.setattr(requests, "get", fake_get)

    result = discover_se_tags("")

    assert result == []
    assert not called


def test_discover_returns_empty_on_all_request_errors(monkeypatch):
    def fake_get(*args, **kwargs):
        raise requests.RequestException("timeout")

    monkeypatch.setattr(requests, "get", fake_get)

    result = discover_se_tags("gaussian", sites=["mattermodeling", "chemistry"])

    assert result == []


def test_discover_skips_failed_sites(monkeypatch):
    def fake_get(url, params=None, **kwargs):
        site = params.get("site", "")
        if site == "chemistry":
            raise requests.RequestException("timeout")
        return _fake_response(200, {"items": [
            {"name": "gaussian", "count": 215},
        ]})

    monkeypatch.setattr(requests, "get", fake_get)

    result = discover_se_tags("gaussian", sites=["mattermodeling", "chemistry"])

    assert len(result) == 1
    assert result[0]["site"] == "mattermodeling"


def test_discover_returns_results_ranked_by_count(monkeypatch):
    def fake_get(url, params=None, **kwargs):
        site = params.get("site", "")
        if site == "mattermodeling":
            return _fake_response(200, {"items": [{"name": "gaussian", "count": 215}]})
        if site == "chemistry":
            return _fake_response(200, {"items": [{"name": "gaussian", "count": 950}]})
        return _fake_response(200, {"items": []})

    monkeypatch.setattr(requests, "get", fake_get)

    result = discover_se_tags("gaussian", sites=["mattermodeling", "chemistry"])

    assert result[0]["count"] == 950
    assert result[1]["count"] == 215


def test_discover_caps_at_max_results(monkeypatch):
    monkeypatch.setattr(stackexchange, "MAX_DISCOVERY_RESULTS", 3)

    items = [{"name": f"tag-{i}", "count": i} for i in range(10)]

    monkeypatch.setattr(
        requests,
        "get",
        lambda *a, **kw: _fake_response(200, {"items": items}),
    )

    result = discover_se_tags("gaussian", sites=["mattermodeling"])

    assert len(result) == 3


def test_discover_happy_path(monkeypatch):
    monkeypatch.setattr(
        requests,
        "get",
        lambda *a, **kw: _fake_response(200, {"items": [
            {"name": "gaussian", "count": 215},
        ]}),
    )

    result = discover_se_tags("gaussian", sites=["mattermodeling"])

    assert len(result) == 1
    assert result[0]["site"] == "mattermodeling"
    assert result[0]["tag"] == "gaussian"
    assert result[0]["count"] == 215
    assert result[0]["label"] == "mattermodeling - gaussian"
