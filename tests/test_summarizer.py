from __future__ import annotations

import requests
from types import SimpleNamespace

from gaussian_scraper.summarizer import summarize_passages


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
