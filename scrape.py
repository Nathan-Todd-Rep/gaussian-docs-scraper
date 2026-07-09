#!/usr/bin/env python3
"""
Domain-agnostic HPC documentation scraper.

Scrapes HTML documentation pages and Stack Exchange questions/answers for
a given research domain (e.g. Gaussian, bioinformatics) and saves the
result to ~/.inkly/{name}_docs.json for Inkly to read at runtime.

Usage:

    py scrape.py                        # launches the interactive setup wizard
    py scrape.py --config gaussian.toml # runs a saved config, no prompts
    py scrape.py --legacy               # uses the original hardcoded Gaussian
                                         # sources in sources.py as a fallback
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from gaussian_scraper.config import ScraperConfig, load_toml_config
from gaussian_scraper.extractor import extract_relevant_passages
from gaussian_scraper.fetcher import fetch_page_text
from gaussian_scraper.sources import GAUSSIAN_KEYWORDS, GAUSSIAN_SOURCES, STACKEXCHANGE_SOURCES
from gaussian_scraper.stackexchange import fetch_se_passages
from gaussian_scraper.summarizer import is_ollama_available, summarize_passages
from gaussian_scraper.wizard import run_wizard


def scrape_html_sources(html_sources: list[dict], keywords: list[str]) -> list[dict]:
    """Scrape HTML documentation pages and return result records."""
    results = []

    for source in html_sources:
        label = source["label"]
        url = source["url"]

        print(f"Fetching: {label}")
        print(f"  URL: {url}")

        text, status = fetch_page_text(url)

        if text is None:
            reason = f"HTTP {status}" if status else "network error"
            print(f"  SKIPPED - {reason}")
            continue

        passages = extract_relevant_passages(text, keywords=keywords)

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


def scrape_se_sources(se_sources: list[dict], keywords: list[str]) -> list[dict]:
    """Fetch top-voted questions from Stack Exchange sources and return result records."""
    results = []

    for source in se_sources:
        label = source["label"]
        tag = source["tag"]
        site = source["site"]

        print(f"Fetching: {label}")
        print(f"  Site: {site}, Tag: {tag}")

        passages = fetch_se_passages(tag=tag, site=site, keywords=keywords)

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

    if not is_ollama_available():
        print("  Ollama not reachable - skipping summarization")
        return

    for result in results:
        label = result["label"]
        print(f"  Summarizing: {label}")
        summary = summarize_passages(result["passages"], label=label)
        if summary:
            result["summary"] = summary
            print(f"  OK")
        else:
            print(f"  SKIPPED - no response from Ollama")


def save_results(results: list[dict], output_path: Path) -> None:
    """Save scraped results to the given output JSON file."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        json.dumps(results, indent=2),
        encoding="utf-8",
    )
    print(f"\nSaved {len(results)} sources to {output_path}")


def build_legacy_config() -> ScraperConfig:
    """
    Build a ScraperConfig from the original hardcoded Gaussian sources in
    sources.py. Kept as a fallback so the scraper still works out of the
    box for Gaussian without touching the config system.
    """
    return ScraperConfig(
        name="gaussian",
        keywords=GAUSSIAN_KEYWORDS,
        html_sources=GAUSSIAN_SOURCES,
        se_sources=STACKEXCHANGE_SOURCES,
    ).validate()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Domain-agnostic HPC documentation scraper.",
    )
    parser.add_argument(
        "--config",
        type=str,
        help="Path to a TOML scraper config. Skips the interactive wizard.",
    )
    parser.add_argument(
        "--legacy",
        action="store_true",
        help="Use the original hardcoded Gaussian sources instead of the config system.",
    )
    return parser.parse_args()


def run_scrape(config: ScraperConfig) -> None:
    """Run the full scrape -> summarize -> save pipeline for a given config."""
    print(f"=== {config.name} Docs Scraper ===\n")

    print("--- HPC Documentation Pages ---")
    results = scrape_html_sources(config.html_sources, config.keywords)

    print("\n--- Stack Exchange ---")
    results += scrape_se_sources(config.se_sources, config.keywords)

    if not results:
        print("\nNo results collected. Check network access or source URLs.")
        return

    summarize_results(results)
    save_results(results, config.output_path)
    total_passages = sum(len(r["passages"]) for r in results)
    print(f"Total passages collected: {total_passages}")


def main() -> None:
    args = parse_args()

    if args.legacy:
        config = build_legacy_config()
    elif args.config:
        config = load_toml_config(Path(args.config))
    else:
        config = run_wizard()

    run_scrape(config)


if __name__ == "__main__":
    main()
