from __future__ import annotations

# Maximum number of passages to keep from a single page.
# Keeps stored snippets focused and avoids flooding the plugin context.
MAX_PASSAGES_PER_SOURCE = 30

# Minimum number of characters a passage must have to be worth keeping.
# Filters out single-word headings and empty lines.
MIN_PASSAGE_LENGTH = 40


def score_passage(passage: str, lower_keywords: list[str]) -> int:
    """
    Score a passage by how many distinct keywords it contains.

    A line mentioning "gaussian", "%mem", and "slurm" together is more
    informative than one that only mentions "gaussian" once, so it should
    be prioritized when a page has more matching lines than the cap allows.
    """
    lower_passage = passage.lower()
    return sum(1 for kw in lower_keywords if kw in lower_passage)


def extract_relevant_passages(text: str, keywords: list[str]) -> list[str]:
    """
    Extract the most keyword-dense passages from raw page text.

    A passage is one line of text from the fetched page. A line is a
    candidate if it's long enough to be meaningful and contains at least
    one keyword (case-insensitive). Exact-duplicate lines are only
    considered once.

    Candidates are ranked by how many distinct keywords they contain (see
    score_passage) and the highest-scoring ones are kept, up to
    MAX_PASSAGES_PER_SOURCE. Ties keep their original document order,
    since sorting is stable and candidates are scored in the order they
    appear in the text. This means a page with more matching lines than
    the cap allows keeps its most substantive content rather than
    whatever happened to appear first.

    Args:
        text: Raw text returned by fetch_page_text().
        keywords: List of keywords to filter by, from the active domain's config.

    Returns:
        A list of unique, relevant passage strings, capped at MAX_PASSAGES_PER_SOURCE.
    """
    lower_keywords = [kw.lower() for kw in keywords]
    candidates = []
    seen = set()

    for line in text.splitlines():
        stripped = line.strip()

        if len(stripped) < MIN_PASSAGE_LENGTH or stripped in seen:
            continue

        score = score_passage(stripped, lower_keywords)
        if score > 0:
            seen.add(stripped)
            candidates.append((score, stripped))

    candidates.sort(key=lambda c: c[0], reverse=True)

    return [passage for _, passage in candidates[:MAX_PASSAGES_PER_SOURCE]]
