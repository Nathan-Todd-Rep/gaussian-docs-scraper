from __future__ import annotations

from gaussian_scraper.dedup import dedupe_across_sources


def test_dedupe_removes_cross_source_duplicates():
    results = [
        {"label": "A", "passages": ["Use %mem=8GB in Gaussian.", "Load module gaussian/16."]},
        {"label": "B", "passages": ["Use %mem=8GB in Gaussian.", "A totally different line."]},
    ]

    deduped, removed = dedupe_across_sources(results)

    assert removed == 1
    assert deduped[0]["passages"] == ["Use %mem=8GB in Gaussian.", "Load module gaussian/16."]
    assert deduped[1]["passages"] == ["A totally different line."]


def test_dedupe_preserves_first_occurrence_source():
    results = [
        {"label": "First", "passages": ["Shared line."]},
        {"label": "Second", "passages": ["Shared line."]},
    ]

    deduped, removed = dedupe_across_sources(results)

    assert len(deduped) == 1
    assert deduped[0]["label"] == "First"
    assert removed == 1


def test_dedupe_drops_source_with_zero_passages_remaining():
    results = [
        {"label": "A", "passages": ["Shared line.", "Unique to A."]},
        {"label": "B", "passages": ["Shared line."]},
    ]

    deduped, removed = dedupe_across_sources(results)

    labels = [r["label"] for r in deduped]
    assert "B" not in labels
    assert removed == 1


def test_dedupe_preserves_order_when_no_duplicates():
    results = [
        {"label": "A", "passages": ["Line one."]},
        {"label": "B", "passages": ["Line two."]},
    ]

    deduped, removed = dedupe_across_sources(results)

    assert removed == 0
    assert [r["label"] for r in deduped] == ["A", "B"]


def test_dedupe_does_not_mutate_input():
    results = [
        {"label": "A", "passages": ["Shared line."]},
        {"label": "B", "passages": ["Shared line."]},
    ]

    dedupe_across_sources(results)

    assert results[1]["passages"] == ["Shared line."]
