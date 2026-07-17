from __future__ import annotations

from gaussian_scraper import source_check
from gaussian_scraper.source_check import check_source, check_sources


def test_check_source_fail_on_network_error(monkeypatch):
    monkeypatch.setattr(source_check, "fetch_page_text", lambda url: (None, None))

    result = check_source("Example", "https://example.com", ["gaussian"])

    assert result["verdict"] == "FAIL"
    assert result["status"] is None
    assert result["keyword_hits"] == 0


def test_check_source_fail_on_non_200(monkeypatch):
    monkeypatch.setattr(source_check, "fetch_page_text", lambda url: (None, 403))

    result = check_source("Example", "https://example.com", ["gaussian"])

    assert result["verdict"] == "FAIL"
    assert result["status"] == 403
    assert "403" in result["reason"]


def test_check_source_empty_when_200_but_no_extractable_content(monkeypatch):
    monkeypatch.setattr(source_check, "fetch_page_text", lambda url: (None, 200))

    result = check_source("Example", "https://example.com", ["gaussian"])

    assert result["verdict"] == "EMPTY"
    assert result["status"] == 200
    assert "JS-rendered" in result["reason"]


def test_check_source_empty_when_no_keyword_matches(monkeypatch):
    monkeypatch.setattr(
        source_check, "fetch_page_text",
        lambda url: ("This page has nothing relevant on it at all.", 200),
    )

    result = check_source("Example", "https://example.com", ["gaussian"])

    assert result["verdict"] == "EMPTY"
    assert result["keyword_hits"] == 0


def test_check_source_weak_below_threshold(monkeypatch):
    monkeypatch.setattr(source_check, "MIN_HITS_GOOD", 10)
    text = "\n".join(["Uses Gaussian for calculations."] * 3)
    monkeypatch.setattr(source_check, "fetch_page_text", lambda url: (text, 200))

    result = check_source("Example", "https://example.com", ["gaussian"])

    assert result["verdict"] == "WEAK"
    assert result["keyword_hits"] == 3


def test_check_source_good_above_threshold(monkeypatch):
    monkeypatch.setattr(source_check, "MIN_HITS_GOOD", 5)
    text = "\n".join(["Uses Gaussian for calculations."] * 10)
    monkeypatch.setattr(source_check, "fetch_page_text", lambda url: (text, 200))

    result = check_source("Example", "https://example.com", ["gaussian"])

    assert result["verdict"] == "GOOD"
    assert result["keyword_hits"] == 10


def test_check_source_is_case_insensitive(monkeypatch):
    monkeypatch.setattr(source_check, "MIN_HITS_GOOD", 1)
    monkeypatch.setattr(source_check, "fetch_page_text", lambda url: ("GAUSSIAN is great.", 200))

    result = check_source("Example", "https://example.com", ["gaussian"])

    assert result["verdict"] == "GOOD"


def test_check_sources_preserves_order(monkeypatch):
    responses = {
        "https://a.com": ("\n".join(["Uses Gaussian for calculations."] * 10), 200),
        "https://b.com": (None, 404),
    }
    monkeypatch.setattr(source_check, "fetch_page_text", lambda url: responses[url])

    sources = [
        {"label": "A", "url": "https://a.com"},
        {"label": "B", "url": "https://b.com"},
    ]
    results = check_sources(sources, ["gaussian"])

    assert results[0]["label"] == "A"
    assert results[0]["verdict"] == "GOOD"
    assert results[1]["label"] == "B"
    assert results[1]["verdict"] == "FAIL"
