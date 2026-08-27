from __future__ import annotations

import pytest

from gaussian_scraper import storage
from gaussian_scraper.passage_index import PassageIndex


def test_search_ranks_relevant_passage_above_unrelated_one():
    records = [
        {
            "label": "Harvard RC - Gaussian",
            "passages": [
                "Set mem and nproc in your Gaussian input file to match your Slurm request.",
                "The cafeteria menu changes weekly.",
            ],
        },
    ]
    index = PassageIndex("gaussian", records)

    matches = index.search("how do I set mem for a Gaussian job?")

    assert matches[0].text.startswith("Set mem and nproc")
    assert matches[0].score > 0.0


def test_search_scores_disjoint_query_as_zero():
    records = [{"label": "A", "passages": ["Load the gaussian module."]}]
    index = PassageIndex("gaussian", records)

    matches = index.search("zxqv unrelated tokens")

    assert all(match.score == 0.0 for match in matches)


def test_search_respects_top_k():
    passages = [f"passage number {i} about gaussian" for i in range(10)]
    records = [{"label": "A", "passages": passages}]
    index = PassageIndex("gaussian", records)

    matches = index.search("gaussian", top_k=3)

    assert len(matches) == 3


def test_search_matches_carry_domain_and_label():
    records = [{"label": "NERSC - Gaussian", "passages": ["Load gaussian/g16."]}]
    index = PassageIndex("gaussian", records)

    matches = index.search("gaussian")

    assert matches[0].domain == "gaussian"
    assert matches[0].label == "NERSC - Gaussian"


def test_index_with_no_passages_returns_no_matches():
    index = PassageIndex("gaussian", [])

    matches = index.search("anything")

    assert matches == []


def test_load_raises_for_missing_domain_file(tmp_path):
    with pytest.raises(FileNotFoundError):
        PassageIndex.load("nonexistent", docs_dir=tmp_path)


def test_load_reads_scraped_sqlite_db_for_domain(tmp_path):
    results = [{"label": "A", "url": "https://example.com", "passages": ["Load the gaussian module."]}]
    storage.save_results(results, tmp_path / "gaussian.db")

    index = PassageIndex.load("gaussian", docs_dir=tmp_path)
    matches = index.search("gaussian module")

    assert matches
    assert matches[0].score > 0.0
