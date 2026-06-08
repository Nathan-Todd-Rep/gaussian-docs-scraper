#!/usr/bin/env python3
"""
Scrape Gaussian documentation from curated HPC sources and save to
~/.inkly/gaussian_docs.json.

Run this to refresh the data:

    py scrape.py

The output file is read by the docs_gaussian plugin in Inkly at runtime.
"""
from __future__ import annotations

import json
from pathlib import Path

from gaussian_scraper.extractor import extract_relevant_passages
from gaussian_scraper.fetcher import fetch_page_text
from gaussian_scraper.sources import GAUSSIAN_SOURCES, STACKEXCHANGE_SOURCES
from gaussian_scraper.stackexchange import fetch_se_passages
from gaussian_scraper.summarizer import summarize_passages

OUTPUT_PATH = Path.home() / ".inkly" / "gaussian_docs.json"


def scrape_html_sources() -> list[dict]:
    """Scrape curated HPC documentation pages and return result records."""
    results = []

    for source in GAUSSIAN_SOURCES:
        label = source["label"]
        url = source["url"]

        print(f"Fetching: {label}")
        print(f"  URL: {url}")

        text = fetch_page_text(url)

        if text is None:
            print(f"  SKIPPED - could not fetch page")
            continue

        passages = extract_relevant_passages(text)

        if not passages:
            print(f"  SKIPPED - no relevant passages found")
            continue

        print(f"  OK - {len(passages)} passages extracted")
        results.append({
            "label": label,
            "url": url,
            "passages": passages,
        })

    return results


def scrape_se_sources() -> list[dict]:
    """Fetch top-voted questions from Stack Exchange sources and return result records."""
    results = []

    for source in STACKEXCHANGE_SOURCES:
        label = source["label"]
        tag = source["tag"]
        site = source["site"]

        print(f"Fetching: {label}")
        print(f"  Site: {site}, Tag: {tag}")

        passages = fetch_se_passages(tag=tag, site=site)

        if passages is None:
            print(f"  SKIPPED - could not reach API")
            continue

        if not passages:
            print(f"  SKIPPED - no relevant passages found")
            continue

        print(f"  OK - {len(passages)} passages extracted")
        results.append({
            "label": label,
            "site": site,
            "tag": tag,
            "passages": passages,
        })

    return results


def summarize_results(results: list[dict]) -> None:
    """Attempt to summarize each result's passages using a local Ollama instance."""
    print("\n--- Summarizing with Ollama ---")
    for result in results:
        label = result["label"]
        print(f"  Summarizing: {label}")
        summary = summarize_passages(result["passages"])
        if summary:
            result["summary"] = summary
            print(f"  OK")
        else:
            print(f"  SKIPPED - Ollama not available or no response")


def save_results(results: list[dict]) -> None:
    """Save scraped results to the output JSON file."""
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(
        json.dumps(results, indent=2),
        encoding="utf-8",
    )
    print(f"\nSaved {len(results)} sources to {OUTPUT_PATH}")


if __name__ == "__main__":
    print("=== Gaussian Docs Scraper ===\n")

    print("--- HPC Documentation Pages ---")
    results = scrape_html_sources()

    print("\n--- Stack Exchange ---")
    results += scrape_se_sources()

    if not results:
        print("\nNo results collected. Check network access or source URLs.")
    else:
        summarize_results(results)
        save_results(results)
        total_passages = sum(len(r["passages"]) for r in results)
        print(f"Total passages collected: {total_passages}")
