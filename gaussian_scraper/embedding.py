from __future__ import annotations

import math
import re
from collections import Counter
from typing import Dict, Iterable, List

# Keeps letters, numbers, underscores, and hyphens together as one token
# (e.g. "%mem" tokenizes to "mem", "gaussian/g16" to "gaussian" and "g16").
TOKEN_RE = re.compile(r"[a-zA-Z0-9_\-]+")


class TfidfEmbedder:
    """
    Small, dependency-free TF-IDF embedder.

    Converts text into a sparse numeric vector so passages can be ranked
    against a query mathematically, without pulling in a real ML/embedding
    library. Deterministic and easy to test -- the tradeoff is that it only
    matches on shared vocabulary, not deeper meaning.
    """

    def __init__(self) -> None:
        self._idf: Dict[str, float] = {}
        self._fitted = False

    @staticmethod
    def tokenize(text: str) -> List[str]:
        if not text:
            return []
        return [tok.lower() for tok in TOKEN_RE.findall(text)]

    def fit(self, texts: Iterable[str]) -> None:
        """
        Learn IDF (inverse document frequency) weights from a corpus.

        Tokens that appear in fewer documents get more weight; tokens that
        appear everywhere (e.g. "the") get less. Must be called before
        encode().
        """
        texts = list(texts)
        num_docs = len(texts)

        if num_docs == 0:
            self._idf = {}
            self._fitted = True
            return

        doc_freq: Counter[str] = Counter()
        for text in texts:
            doc_freq.update(set(self.tokenize(text)))

        # Smoothed IDF: log((1 + num_docs) / (1 + freq)) + 1.
        # Smoothing avoids division by zero and keeps values stable for
        # tokens that appear in almost every document.
        self._idf = {
            token: math.log((1.0 + num_docs) / (1.0 + freq)) + 1.0
            for token, freq in doc_freq.items()
        }
        self._fitted = True

    def encode(self, text: str) -> Dict[str, float]:
        """Encode one string into a normalized, sparse TF-IDF vector."""
        if not self._fitted:
            raise RuntimeError("TfidfEmbedder must be fitted before encode()")

        tokens = self.tokenize(text)
        if not tokens:
            return {}

        counts = Counter(tokens)
        total = float(sum(counts.values()))

        vec: Dict[str, float] = {}
        for token, count in counts.items():
            # Tokens never seen during fit() get no weight -- they carry
            # no information about relative importance across the corpus.
            if token not in self._idf:
                continue
            tf = count / total
            vec[token] = tf * self._idf[token]

        return self._normalize(vec)

    @staticmethod
    def _normalize(vec: Dict[str, float]) -> Dict[str, float]:
        if not vec:
            return {}
        norm = math.sqrt(sum(v * v for v in vec.values()))
        if norm == 0.0:
            return dict(vec)
        return {k: v / norm for k, v in vec.items()}


def cosine_similarity(left: Dict[str, float], right: Dict[str, float]) -> float:
    """
    Cosine similarity between two sparse TF-IDF vectors.

    Returns 0.0 if either vector is empty (e.g. a query or passage that
    shares no vocabulary with the fitted corpus).
    """
    if not left or not right:
        return 0.0

    # Iterate over the smaller vector to reduce lookup work.
    if len(left) > len(right):
        left, right = right, left

    return sum(value * right.get(token, 0.0) for token, value in left.items())
