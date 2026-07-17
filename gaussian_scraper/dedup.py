from __future__ import annotations


def dedupe_across_sources(results: list[dict]) -> tuple[list[dict], int]:
    """
    Remove passages that are exact duplicates of a passage already kept by
    an earlier source in the list.

    As more overlapping Stack Exchange tags are added (e.g. a question
    tagged both "gaussian" and "computational-chemistry"), the same
    question or answer can be fetched multiple times under different
    source labels. This keeps the first occurrence and drops the rest,
    so the same content isn't duplicated across the final dataset.

    Within-source duplication is already handled by extractor.py and
    stackexchange.py at extraction time -- this only catches duplicates
    that span two different sources.

    Order of results and of passages within each result is preserved.
    A source that ends up with zero passages after dedup is dropped
    entirely from the returned list.

    Returns a tuple of (deduped_results, total_duplicates_removed).
    """
    seen = set()
    deduped_results = []
    total_removed = 0

    for result in results:
        unique_passages = []
        for passage in result["passages"]:
            if passage in seen:
                total_removed += 1
                continue
            seen.add(passage)
            unique_passages.append(passage)

        if unique_passages:
            new_result = dict(result)
            new_result["passages"] = unique_passages
            deduped_results.append(new_result)

    return deduped_results, total_removed
