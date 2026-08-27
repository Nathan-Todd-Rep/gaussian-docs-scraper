from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import List

from gaussian_scraper import storage
from gaussian_scraper.config import DEFAULT_OUTPUT_DIR
from gaussian_scraper.embedding import TfidfEmbedder, cosine_similarity


@dataclass(frozen=True)
class PassageMatch:
    """One scraped passage ranked against a query."""

    domain: str
    label: str
    text: str
    score: float


class PassageIndex:
    """
    Ranks one domain's scraped passages against a query.

    This is the retrieval half of a RAG-style pipeline: the scraper already
    collects and stores passages per domain (see scrape.py); this ranks
    them so a consumer -- Inkly, or anything else -- can pull back only the
    handful of passages relevant to a specific question instead of every
    passage a domain has ever collected. Dumping everything into an LLM
    prompt regardless of the question doesn't scale: prompt size grows
    with total scraped volume instead of staying bounded, and the model
    has to sift through mostly-irrelevant text to find what matters.

    Built directly from the SQLite database a scrape run produces -- no
    extra scrape step needed.
    """

    def __init__(self, domain: str, records: list[dict]):
        self.domain = domain
        self._embedder = TfidfEmbedder()

        # One (label, passage text) pair per scraped passage, flattened
        # across every source in the domain.
        self._entries: List[tuple[str, str]] = [
            (source.get("label", "Unknown source"), passage)
            for source in records
            for passage in source.get("passages", [])
        ]

        self._embedder.fit(text for _, text in self._entries)
        self._vectors = [self._embedder.encode(text) for _, text in self._entries]

    @classmethod
    def load(cls, domain: str, docs_dir: Path | None = None) -> "PassageIndex":
        """
        Build a PassageIndex from a domain's SQLite database.

        Reads from the same default location scrape.py writes to
        (~/.inkly/{domain}.db unless a config overrides it), so no
        extra setup is needed beyond having already run the scraper for
        that domain.
        """
        docs_dir = docs_dir or DEFAULT_OUTPUT_DIR
        db_path = Path(docs_dir) / f"{domain}.db"
        records = storage.load_domain_records(domain, db_path)
        return cls(domain, records)

    def search(self, query: str, *, top_k: int = 5) -> List[PassageMatch]:
        """
        Return the top_k passages most relevant to query, ranked by cosine
        similarity, highest first.

        A passage scored 0.0 shares no known vocabulary with the query --
        callers should generally treat that as "no match" rather than a
        genuine result, since ties at 0.0 are effectively unranked.
        """
        query_vector = self._embedder.encode(query)

        scored = [
            PassageMatch(domain=self.domain, label=label, text=text, score=score)
            for (label, text), score in zip(
                self._entries,
                (cosine_similarity(query_vector, vector) for vector in self._vectors),
            )
        ]

        scored.sort(key=lambda match: match.score, reverse=True)
        return scored[:top_k]
