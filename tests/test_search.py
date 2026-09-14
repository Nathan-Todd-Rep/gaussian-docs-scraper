from __future__ import annotations

import pytest

from gaussian_scraper import storage
from gaussian_scraper.search import search_docs


def test_search_docs_reads_domain_database(tmp_path):
    results = [
        {
            "label": "Gaussian Docs",
            "url": "https://example.com",
            "passages": [
                "Use %mem in the Gaussian input file to set memory.",
                "This passage is unrelated to memory settings.",
            ],
        }
    ]
    storage.save_results(results, tmp_path / "gaussian.db")

    matches = search_docs(
        "gaussian",
        "how do I set Gaussian memory?",
        top_k=1,
        docs_dir=tmp_path,
    )

    assert len(matches) == 1
    assert matches[0].domain == "gaussian"
    assert matches[0].label == "Gaussian Docs"
    assert matches[0].score > 0.0


def test_search_docs_raises_for_missing_domain(tmp_path):
    with pytest.raises(FileNotFoundError):
        search_docs(
            "missing-domain",
            "anything",
            docs_dir=tmp_path,
        )
