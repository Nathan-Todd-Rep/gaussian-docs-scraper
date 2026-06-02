from __future__ import annotations

import requests
from bs4 import BeautifulSoup

from gaussian_scraper.extractor import MAX_PASSAGES_PER_SOURCE, MIN_PASSAGE_LENGTH
from gaussian_scraper.sources import GAUSSIAN_KEYWORDS

SE_API_BASE = "https://api.stackexchange.com/2.3"
REQUEST_TIMEOUT_SEC = 10


def _strip_html(html: str) -> str:
    return BeautifulSoup(html, "html.parser").get_text(separator=" ", strip=True)


def fetch_se_passages(
    tag: str,
    site: str = "chemistry",
    max_questions: int = 20,
    keywords: list[str] | None = None,
) -> list[str] | None:
    """
    Fetch top-voted questions from a Stack Exchange site by tag and return
    relevant passages.

    Each question contributes two kinds of passages:
    - The question title, if it contains a keyword
    - Lines from the question body, filtered the same way as HTML page text

    Returns None if the request fails. Returns an empty list if the request
    succeeds but no relevant passages are found.
    """
    if keywords is None:
        keywords = GAUSSIAN_KEYWORDS

    lower_keywords = [kw.lower() for kw in keywords]

    try:
        response = requests.get(
            f"{SE_API_BASE}/questions",
            params={
                "tagged": tag,
                "site": site,
                "filter": "withbody",
                "pagesize": max_questions,
                "order": "desc",
                "sort": "votes",
            },
            timeout=REQUEST_TIMEOUT_SEC,
        )
    except requests.RequestException:
        return None

    if response.status_code != 200:
        return None

    try:
        data = response.json()
    except ValueError:
        return None

    passages = []

    for question in data.get("items", []):
        title = question.get("title", "")
        body_text = _strip_html(question.get("body", ""))

        if (
            len(title) >= MIN_PASSAGE_LENGTH
            and any(kw in title.lower() for kw in lower_keywords)
        ):
            passages.append(title)
            if len(passages) >= MAX_PASSAGES_PER_SOURCE:
                return passages

        for line in body_text.splitlines():
            stripped = line.strip()
            if len(stripped) < MIN_PASSAGE_LENGTH:
                continue
            if any(kw in stripped.lower() for kw in lower_keywords):
                passages.append(stripped)
            if len(passages) >= MAX_PASSAGES_PER_SOURCE:
                return passages

    return passages if passages else None
