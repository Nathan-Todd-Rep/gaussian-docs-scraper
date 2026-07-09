from __future__ import annotations

from gaussian_scraper.fetcher import fetch_page_text

# Minimum keyword hits for a source to be considered reliably on-topic.
# Below this a page might mention the topic in passing but not be a
# substantive documentation source -- based on manually vetted sources,
# which ranged from 28-66 hits for genuinely good pages.
MIN_HITS_GOOD = 10

# 1+ hits but below MIN_HITS_GOOD: on-topic but thin. Worth a human look
# before adding to a preset rather than auto-including.
MIN_HITS_WEAK = 1


def _count_keyword_hits(text: str, keywords: list[str]) -> int:
    """Count how many lines in text contain at least one keyword."""
    lower_keywords = [kw.lower() for kw in keywords]
    hits = 0
    for line in text.splitlines():
        lower_line = line.lower()
        if any(kw in lower_line for kw in lower_keywords):
            hits += 1
    return hits


def check_source(label: str, url: str, keywords: list[str]) -> dict:
    """
    Fetch a candidate URL and classify how suitable it is as a scrape source.

    Verdicts:
        FAIL  - network error or non-200 HTTP status. Source is unusable.
        EMPTY - 200 status but no extractable text at all. Usually means
                the page content is JS-rendered and invisible to
                BeautifulSoup (seen with Alliance Canada wiki pages).
        WEAK  - some text extracted but few keyword hits. Might be
                tangentially related; needs a human look before trusting it.
        GOOD  - text extracted with strong keyword density. Safe to add.

    Returns a dict with label, url, status, verdict, keyword_hits, and
    a short human-readable reason.
    """
    text, status = fetch_page_text(url)

    if text is None and status is None:
        return {
            "label": label, "url": url, "status": None,
            "verdict": "FAIL", "keyword_hits": 0,
            "reason": "network error",
        }

    if text is None:
        return {
            "label": label, "url": url, "status": status,
            "verdict": "FAIL", "keyword_hits": 0,
            "reason": f"HTTP {status}",
        }

    hits = _count_keyword_hits(text, keywords)

    if hits == 0:
        return {
            "label": label, "url": url, "status": status,
            "verdict": "EMPTY", "keyword_hits": 0,
            "reason": "no keyword matches -- page may be JS-rendered or off-topic",
        }

    if hits < MIN_HITS_GOOD:
        return {
            "label": label, "url": url, "status": status,
            "verdict": "WEAK", "keyword_hits": hits,
            "reason": f"only {hits} keyword hit(s) -- review before trusting",
        }

    return {
        "label": label, "url": url, "status": status,
        "verdict": "GOOD", "keyword_hits": hits,
        "reason": f"{hits} keyword hits",
    }


def check_sources(sources: list[dict], keywords: list[str]) -> list[dict]:
    """
    Check a batch of candidate {label, url} sources and return their
    verdicts. Order is preserved so results can be matched back to input.
    """
    return [check_source(s["label"], s["url"], keywords) for s in sources]
