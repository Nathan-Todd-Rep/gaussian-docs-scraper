from __future__ import annotations

import requests
from bs4 import BeautifulSoup

from gaussian_scraper.extractor import MAX_PASSAGES_PER_SOURCE, MIN_PASSAGE_LENGTH
from gaussian_scraper.sources import GAUSSIAN_KEYWORDS

SE_API_BASE = "https://api.stackexchange.com/2.3"
REQUEST_TIMEOUT_SEC = 10

# SE sites searched during tag auto-discovery.
# Covers the main research computing and computational science communities.
DEFAULT_DISCOVERY_SITES = [
    "mattermodeling",
    "chemistry",
    "bioinformatics",
    "scicomp",
]

MAX_DISCOVERY_RESULTS = 10


def _strip_html(html: str) -> str:
    return BeautifulSoup(html, "html.parser").get_text(separator=" ", strip=True)


def _fetch_answer_bodies(question_ids: list[int], site: str) -> list[str]:
    """
    Fetch answer bodies for the given question IDs.
    Returns a list of plain text strings sorted by vote score.
    Returns an empty list on any failure so callers can degrade gracefully.
    """
    if not question_ids:
        return []

    ids_str = ";".join(str(i) for i in question_ids)

    try:
        response = requests.get(
            f"{SE_API_BASE}/questions/{ids_str}/answers",
            params={
                "site": site,
                "filter": "withbody",
                "order": "desc",
                "sort": "votes",
                "pagesize": min(len(question_ids) * 2, 100),
            },
            timeout=REQUEST_TIMEOUT_SEC,
        )
    except requests.RequestException:
        return []

    if response.status_code != 200:
        return []

    try:
        data = response.json()
    except ValueError:
        return []

    bodies = []
    for answer in data.get("items", []):
        body_text = _strip_html(answer.get("body", ""))
        if body_text:
            bodies.append(body_text)

    return bodies


def fetch_se_passages(
    tag: str,
    site: str = "chemistry",
    max_questions: int = 20,
    keywords: list[str] | None = None,
) -> list[str] | None:
    """
    Fetch top-voted questions and their answers from a Stack Exchange site
    by tag and return relevant passages.

    Each question contributes passages from:
    - The question title, if it contains a keyword
    - Lines from the question body, filtered the same way as HTML page text
    - Lines from the top answers to those questions

    Exact-duplicate lines (e.g. a question's title repeated verbatim in its
    body, or a boilerplate line reused across answers) are only kept once
    across the whole call, so the cap isn't wasted on repeated content.

    Returns None if the questions request fails. Returns an empty list if
    the request succeeds but no relevant passages are found.
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
    seen = set()
    question_ids = []

    for question in data.get("items", []):
        question_ids.append(question.get("question_id"))

        if len(passages) >= MAX_PASSAGES_PER_SOURCE:
            continue

        title = question.get("title", "")
        body_text = _strip_html(question.get("body", ""))

        if (
            len(title) >= MIN_PASSAGE_LENGTH
            and any(kw in title.lower() for kw in lower_keywords)
            and title not in seen
        ):
            seen.add(title)
            passages.append(title)
            if len(passages) >= MAX_PASSAGES_PER_SOURCE:
                continue

        for line in body_text.splitlines():
            stripped = line.strip()
            if len(stripped) < MIN_PASSAGE_LENGTH:
                continue
            if any(kw in stripped.lower() for kw in lower_keywords) and stripped not in seen:
                seen.add(stripped)
                passages.append(stripped)
            if len(passages) >= MAX_PASSAGES_PER_SOURCE:
                break

    if question_ids and len(passages) < MAX_PASSAGES_PER_SOURCE:
        for body_text in _fetch_answer_bodies(question_ids, site):
            for line in body_text.splitlines():
                stripped = line.strip()
                if len(stripped) < MIN_PASSAGE_LENGTH:
                    continue
                if any(kw in stripped.lower() for kw in lower_keywords) and stripped not in seen:
                    seen.add(stripped)
                    passages.append(stripped)
                if len(passages) >= MAX_PASSAGES_PER_SOURCE:
                    return passages

    return passages if passages else None


def discover_se_tags(
    topic: str,
    sites: list[str] | None = None,
) -> list[dict]:
    """
    Search Stack Exchange sites for tags matching the given topic string.

    Queries the SE tags endpoint with inname={topic} across each site and
    returns up to MAX_DISCOVERY_RESULTS results ranked by question count.

    Each result is a dict with:
        site:  SE site identifier (e.g. "mattermodeling")
        tag:   Tag name (e.g. "gaussian")
        count: Number of questions with this tag
        label: Human-readable label for use in configs and output

    Returns an empty list if no matching tags are found or all requests fail.
    """
    if not topic or not topic.strip():
        return []

    if sites is None:
        sites = DEFAULT_DISCOVERY_SITES

    results = []

    for site in sites:
        try:
            response = requests.get(
                f"{SE_API_BASE}/tags",
                params={
                    "site": site,
                    "inname": topic.strip(),
                    "order": "desc",
                    "sort": "popular",
                    "pagesize": MAX_DISCOVERY_RESULTS,
                },
                timeout=REQUEST_TIMEOUT_SEC,
            )
        except requests.RequestException:
            continue

        if response.status_code != 200:
            continue

        try:
            data = response.json()
        except ValueError:
            continue

        for item in data.get("items", []):
            tag = item.get("name", "")
            count = item.get("count", 0)
            if tag:
                results.append({
                    "site": site,
                    "tag": tag,
                    "count": count,
                    "label": f"{site} - {tag}",
                })

    results.sort(key=lambda r: r["count"], reverse=True)
    return results[:MAX_DISCOVERY_RESULTS]
