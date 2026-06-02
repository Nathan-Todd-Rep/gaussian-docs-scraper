from __future__ import annotations

import requests
from types import SimpleNamespace
import json

from gaussian_scraper import stackexchange
from gaussian_scraper.stackexchange import fetch_se_passages


def _fake_response(status_code: int, data: dict):
    """Build a fake requests response that returns JSON."""
    ns = SimpleNamespace(
        status_code=status_code,
        json=lambda: data,
    )
    return ns


SAMPLE_QUESTION = {
    "question_id": 1,
    "title": "How do I set %mem and %nproc in Gaussian 16 for a Slurm job?",
    "body": "<p>I am trying to run a Gaussian g16 DFT calculation on an HPC cluster.</p>"
            "<p>What values should I use for %mem and %nproc in my input file?</p>",
    "score": 42,
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


def test_fetch_se_returns_empty_list_when_no_items(monkeypatch):
    monkeypatch.setattr(
        requests,
        "get",
        lambda *a, **kw: _fake_response(200, {"items": [], "has_more": False}),
    )

    result = fetch_se_passages(tag="gaussian", site="chemistry")

    assert result is None


# --- passage extraction ---

def test_fetch_se_extracts_title_as_passage(monkeypatch):
    monkeypatch.setattr(
        requests,
        "get",
        lambda *a, **kw: _fake_response(200, {"items": [SAMPLE_QUESTION]}),
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
        lambda *a, **kw: _fake_response(200, {"items": [question]}),
    )

    result = fetch_se_passages(tag="gaussian", site="chemistry")

    assert result is not None
    # HTML tags should be gone
    assert all("<" not in p for p in result)
    # Text content should be present
    assert any("%mem" in p or "Gaussian" in p for p in result)


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
        lambda *a, **kw: _fake_response(200, {"items": items}),
    )

    result = fetch_se_passages(tag="gaussian", site="chemistry")

    assert result is not None
    assert len(result) == 3
