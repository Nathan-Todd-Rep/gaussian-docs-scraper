from __future__ import annotations

import requests
from types import SimpleNamespace

from gaussian_scraper import summarizer
from gaussian_scraper.summarizer import is_ollama_available, summarize_passages


def _fake_response(status_code: int, data: dict):
    return SimpleNamespace(
        status_code=status_code,
        json=lambda: data,
    )


SAMPLE_PASSAGES = [
    "Set %mem=8GB and %nproc=4 in your Gaussian input file to match your Slurm resource request.",
    "Gaussian 16 requires the %chk directive to save checkpoint files for post-processing.",
    "Use g16 with a Slurm batch script to run DFT calculations on HPC clusters.",
]


# --- is_ollama_available ---

def test_is_ollama_available_returns_true_when_reachable(monkeypatch):
    monkeypatch.setattr(
        requests,
        "get",
        lambda *a, **kw: SimpleNamespace(status_code=200),
    )

    assert is_ollama_available() is True


def test_is_ollama_available_returns_false_when_not_reachable(monkeypatch):
    def fake_get(*args, **kwargs):
        raise requests.RequestException("connection refused")

    monkeypatch.setattr(requests, "get", fake_get)

    assert is_ollama_available() is False


def test_is_ollama_available_returns_false_on_non_200(monkeypatch):
    monkeypatch.setattr(
        requests,
        "get",
        lambda *a, **kw: SimpleNamespace(status_code=503),
    )

    assert is_ollama_available() is False


# --- failure cases ---

def test_summarize_returns_none_on_request_error(monkeypatch):
    def fake_post(*args, **kwargs):
        raise requests.RequestException("connection refused")

    monkeypatch.setattr(requests, "post", fake_post)

    result = summarize_passages(SAMPLE_PASSAGES)

    assert result is None


def test_summarize_returns_none_on_non_200(monkeypatch):
    monkeypatch.setattr(
        requests,
        "post",
        lambda *a, **kw: _fake_response(500, {}),
    )

    result = summarize_passages(SAMPLE_PASSAGES)

    assert result is None


def test_summarize_returns_none_on_bad_json(monkeypatch):
    def fake_post(*args, **kwargs):
        return SimpleNamespace(
            status_code=200,
            json=lambda: (_ for _ in ()).throw(ValueError("not json")),
        )

    monkeypatch.setattr(requests, "post", fake_post)

    result = summarize_passages(SAMPLE_PASSAGES)

    assert result is None


def test_summarize_returns_none_on_empty_response_field(monkeypatch):
    monkeypatch.setattr(
        requests,
        "post",
        lambda *a, **kw: _fake_response(200, {"response": "   "}),
    )

    result = summarize_passages(SAMPLE_PASSAGES)

    assert result is None


# --- anti-hallucination instructions ---

def test_summarize_prompt_forbids_outside_information(monkeypatch):
    captured_prompt = []

    def fake_post(url, json=None, **kwargs):
        captured_prompt.append(json.get("prompt", ""))
        return SimpleNamespace(
            status_code=200,
            json=lambda: {"response": "A summary."},
        )

    monkeypatch.setattr(requests, "post", fake_post)

    summarize_passages(SAMPLE_PASSAGES)

    prompt = captured_prompt[0].lower()
    assert "not directly stated in the passages" in prompt
    assert "do not rely on outside knowledge" in prompt
    assert "say so plainly rather than guessing" in prompt


# --- passage cap ---

def test_summarize_caps_passages_sent_to_ollama(monkeypatch):
    monkeypatch.setattr(summarizer, "MAX_PASSAGES_TO_SUMMARIZE", 3)

    captured_prompt = []

    def fake_post(url, json=None, **kwargs):
        captured_prompt.append(json.get("prompt", ""))
        return SimpleNamespace(
            status_code=200,
            json=lambda: {"response": "A summary."},
        )

    monkeypatch.setattr(requests, "post", fake_post)

    passages = [f"Passage number {i} about Gaussian on the HPC cluster." for i in range(10)]
    summarize_passages(passages)

    assert len(captured_prompt) == 1
    prompt = captured_prompt[0]
    assert "Passage number 0" in prompt
    assert "Passage number 2" in prompt
    assert "Passage number 3" not in prompt


# --- happy path ---

def test_summarize_returns_summary_string(monkeypatch):
    expected = "Gaussian 16 jobs on HPC clusters should set %mem and %nproc to match Slurm resource requests."

    monkeypatch.setattr(
        requests,
        "post",
        lambda *a, **kw: _fake_response(200, {"response": expected}),
    )

    result = summarize_passages(SAMPLE_PASSAGES)

    assert result == expected


# --- timeout ---

def test_summarize_passes_custom_timeout_to_request(monkeypatch):
    captured_timeouts = []

    def fake_post(url, json=None, timeout=None, **kwargs):
        captured_timeouts.append(timeout)
        return _fake_response(200, {"response": "A summary."})

    monkeypatch.setattr(requests, "post", fake_post)

    summarize_passages(SAMPLE_PASSAGES, timeout=180)

    assert captured_timeouts == [180]


def test_summarize_uses_default_timeout_when_not_specified(monkeypatch):
    captured_timeouts = []

    def fake_post(url, json=None, timeout=None, **kwargs):
        captured_timeouts.append(timeout)
        return _fake_response(200, {"response": "A summary."})

    monkeypatch.setattr(requests, "post", fake_post)

    summarize_passages(SAMPLE_PASSAGES)

    assert captured_timeouts == [summarizer.REQUEST_TIMEOUT_SEC]


# --- edge cases ---

def test_summarize_returns_none_for_empty_passages(monkeypatch):
    called = []

    def fake_post(*args, **kwargs):
        called.append(True)
        return _fake_response(200, {"response": "should not be called"})

    monkeypatch.setattr(requests, "post", fake_post)

    result = summarize_passages([])

    assert result is None
    assert not called
