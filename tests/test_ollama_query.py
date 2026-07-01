from __future__ import annotations

import requests
from types import SimpleNamespace

from gaussian_scraper.ollama_query import is_gaussian_query, query_gaussian


def _fake_response(status_code: int, data: dict):
    return SimpleNamespace(
        status_code=status_code,
        json=lambda: data,
    )


# --- is_gaussian_query ---

def test_is_gaussian_query_returns_true_for_keyword_match():
    assert is_gaussian_query("How do I run a gaussian calculation on the cluster?") is True


def test_is_gaussian_query_is_case_insensitive():
    assert is_gaussian_query("What is the difference between G09 and G16?") is True
    assert is_gaussian_query("How do I set %MEM in GAUSSIAN?") is True


def test_is_gaussian_query_returns_false_for_unrelated_text():
    assert is_gaussian_query("What is the weather like today?") is False


# --- query_gaussian failure cases ---

def test_query_gaussian_returns_none_on_request_error(monkeypatch):
    def fake_post(*args, **kwargs):
        raise requests.RequestException("connection refused")

    monkeypatch.setattr(requests, "post", fake_post)

    result = query_gaussian("How do I set %mem in Gaussian 16?")

    assert result is None


def test_query_gaussian_returns_none_on_non_200(monkeypatch):
    monkeypatch.setattr(
        requests,
        "post",
        lambda *a, **kw: _fake_response(500, {}),
    )

    result = query_gaussian("How do I set %mem in Gaussian 16?")

    assert result is None


def test_query_gaussian_returns_none_on_bad_json(monkeypatch):
    def fake_post(*args, **kwargs):
        return SimpleNamespace(
            status_code=200,
            json=lambda: (_ for _ in ()).throw(ValueError("not json")),
        )

    monkeypatch.setattr(requests, "post", fake_post)

    result = query_gaussian("How do I set %mem in Gaussian 16?")

    assert result is None


def test_query_gaussian_returns_none_on_empty_response_field(monkeypatch):
    monkeypatch.setattr(
        requests,
        "post",
        lambda *a, **kw: _fake_response(200, {"response": "   "}),
    )

    result = query_gaussian("How do I set %mem in Gaussian 16?")

    assert result is None


def test_query_gaussian_returns_none_for_empty_topic(monkeypatch):
    called = []

    def fake_post(*args, **kwargs):
        called.append(True)
        return _fake_response(200, {"response": "should not be called"})

    monkeypatch.setattr(requests, "post", fake_post)

    result = query_gaussian("")

    assert result is None
    assert not called


# --- query_gaussian happy path ---

def test_query_gaussian_returns_answer_string(monkeypatch):
    expected = "Set %mem=8GB and %nproc=4 in your Gaussian input file to match your Slurm resource request."

    monkeypatch.setattr(
        requests,
        "post",
        lambda *a, **kw: _fake_response(200, {"response": expected}),
    )

    result = query_gaussian("How do I set memory in Gaussian 16?")

    assert result == expected
