from __future__ import annotations

import pytest

from gaussian_scraper.embedding import TfidfEmbedder, cosine_similarity


def test_tokenize_lowercases_and_splits_on_punctuation():
    assert TfidfEmbedder.tokenize("Set %mem=8GB for Gaussian/g16!") == [
        "set", "mem", "8gb", "for", "gaussian", "g16",
    ]


def test_tokenize_returns_empty_list_for_blank_text():
    assert TfidfEmbedder.tokenize("") == []


def test_encode_raises_before_fit():
    embedder = TfidfEmbedder()
    with pytest.raises(RuntimeError):
        embedder.encode("gaussian")


def test_encode_returns_empty_vector_for_unseen_tokens():
    embedder = TfidfEmbedder()
    embedder.fit(["gaussian module load"])

    vector = embedder.encode("completely different words")

    assert vector == {}


def test_encode_gives_more_weight_to_rare_tokens():
    embedder = TfidfEmbedder()
    embedder.fit([
        "gaussian module load command",
        "gaussian job submission steps",
        "gaussian memory settings",
    ])

    vector = embedder.encode("gaussian memory settings")

    # "gaussian" appears in every document (low IDF); "memory" and
    # "settings" appear in only one (higher IDF), so they should carry
    # more weight in the resulting vector.
    assert vector["memory"] > vector["gaussian"]


def test_cosine_similarity_is_1_for_identical_text():
    embedder = TfidfEmbedder()
    embedder.fit(["gaussian module load", "unrelated other text"])

    vec = embedder.encode("gaussian module load")

    assert cosine_similarity(vec, vec) == pytest.approx(1.0)


def test_cosine_similarity_is_0_for_disjoint_vocabulary():
    embedder = TfidfEmbedder()
    embedder.fit(["gaussian module load", "unrelated other text"])

    left = embedder.encode("gaussian module load")
    right = embedder.encode("unrelated other text")

    assert cosine_similarity(left, right) == 0.0


def test_cosine_similarity_handles_empty_vectors():
    assert cosine_similarity({}, {"gaussian": 1.0}) == 0.0
    assert cosine_similarity({}, {}) == 0.0


def test_fit_on_empty_corpus_does_not_crash():
    embedder = TfidfEmbedder()
    embedder.fit([])

    assert embedder.encode("anything") == {}
