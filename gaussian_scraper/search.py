from __future__ import annotations

from pathlib import Path
from typing import List

from gaussian_scraper.passage_index import PassageIndex, PassageMatch


def search_docs(
    domain: str,
    query: str,
    *,
    top_k: int = 5,
    tool: str | None = None,
    docs_dir: Path | None = None,
) -> List[PassageMatch]:
    """Search one scraped documentation domain for passages relevant to query."""
    index = PassageIndex.load(domain, docs_dir=docs_dir)
    return index.search(query, top_k=top_k, tool=tool)
