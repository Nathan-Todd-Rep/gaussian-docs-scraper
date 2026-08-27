#!/usr/bin/env python3
"""
Domain-agnostic HPC documentation scraper.

Scrapes HTML documentation pages and Stack Exchange questions/answers for
a given research domain (e.g. Gaussian, bioinformatics) and saves the
result to ~/.inkly/{name}_docs.json for Inkly to read at runtime.

Usage:

    py scrape.py                        # launches the interactive setup wizard
    py scrape.py --list-configs         # shows configs you've already saved
    py scrape.py --config gaussian.toml # runs a saved config, no prompts

Run "py scrape.py --help" for the full option list with examples.
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

from gaussian_scraper.config import ConfigError, ScraperConfig, load_toml_config
from gaussian_scraper.dedup import dedupe_across_sources
from gaussian_scraper.extractor import extract_relevant_passages
from gaussian_scraper.fetcher import fetch_page_text
from gaussian_scraper.stackexchange import fetch_se_passages
from gaussian_scraper.summarizer import (
    OLLAMA_MODEL,
    REQUEST_TIMEOUT_SEC,
    is_ollama_available,
    summarize_passages,
)
from gaussian_scraper.wizard import run_wizard

# Directory the wizard offers by default when saving configs; also where
# --list-configs looks, so users never need to know or type a path.
CONFIG_DIR = Path("configs")


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

        passages = fetch_se_passages(tag=tag, keywords=keywords, site=site)

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


def summarize_results(
    results: list[dict],
    model: str = OLLAMA_MODEL,
    timeout: float = REQUEST_TIMEOUT_SEC,
) -> None:
    """Attempt to summarize each result's passages using a local Ollama instance."""
    print(f"\n--- Summarizing with Ollama (model: {model}, timeout: {timeout:g}s) ---")

    if not is_ollama_available():
        print("  Ollama not reachable - skipping summarization")
        return

    for result in results:
        label = result["label"]
        print(f"  Summarizing: {label}")
        summary = summarize_passages(result["passages"], label=label, model=model, timeout=timeout)
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


def list_configs(config_dir: Path) -> None:
    """Print the saved TOML configs in config_dir, so users don't need to know file paths."""
    if not config_dir.is_dir():
        print(f"No configs found -- '{config_dir}' does not exist yet.")
        return

    toml_files = sorted(config_dir.glob("*.toml"))
    if not toml_files:
        print(f"No saved configs in '{config_dir}' yet. Run 'py scrape.py' to create one.")
        return

    print(f"Saved configs in '{config_dir}':\n")
    for path in toml_files:
        try:
            config = load_toml_config(path)
            source_count = len(config.html_sources) + len(config.se_sources)
            print(f"  {path.name:<30} {config.name} -- {source_count} source(s), "
                  f"{len(config.keywords)} keyword(s)")
        except ConfigError as e:
            print(f"  {path.name:<30} INVALID -- {e}")
    print(f"\nRun a saved config with: py scrape.py --config {config_dir}/<name>.toml")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Domain-agnostic HPC documentation scraper for Inkly. "
                     "Collects HPC/research documentation and Stack Exchange "
                     "passages for a topic and saves them for Inkly to read.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "examples:\n"
            "  py scrape.py                          run the guided setup wizard (recommended --\n"
            "                                        no prior config needed, just answer prompts)\n"
            "  py scrape.py --list-configs           show configs you've already saved\n"
            "  py scrape.py --config configs/gaussian.toml\n"
            "                                        re-run a saved config with no prompts\n"
            "  py scrape.py --model llama3-cuttlefish\n"
            "                                        use a different Ollama model for summaries\n"
            "  py scrape.py --summary-timeout 180    give slow/CPU-only Ollama more time per summary\n"
            "  py scrape.py --skip-summary           just scrape raw passages, no Ollama at all\n"
        ),
    )
    parser.add_argument(
        "--config",
        type=str,
        metavar="PATH",
        help="Path to a saved TOML config (see --list-configs). Skips the wizard.",
    )
    parser.add_argument(
        "--list-configs",
        action="store_true",
        help="List saved configs in the configs/ folder and exit.",
    )
    parser.add_argument(
        "--model",
        type=str,
        default=OLLAMA_MODEL,
        help=f"Ollama model to use for summarization (default: {OLLAMA_MODEL}). "
             f"Ignored if Ollama isn't running.",
    )
    parser.add_argument(
        "--summary-timeout",
        type=float,
        default=REQUEST_TIMEOUT_SEC,
        metavar="SECONDS",
        help=f"Seconds to wait per summarization request (default: {REQUEST_TIMEOUT_SEC:g}). "
             f"CPU-only Ollama can be slow -- raise this if summaries keep getting "
             f"skipped even though Ollama is running.",
    )
    parser.add_argument(
        "--skip-summary",
        action="store_true",
        help="Skip Ollama summarization entirely and just scrape raw passages. "
             "Much faster on CPU-only machines; Inkly's retrieval reads raw "
             "passages either way, so summaries aren't required for that.",
    )
    return parser.parse_args()


def run_scrape(
    config: ScraperConfig,
    model: str = OLLAMA_MODEL,
    summary_timeout: float = REQUEST_TIMEOUT_SEC,
    skip_summary: bool = False,
) -> None:
    """Run the full scrape -> summarize -> save pipeline for a given config."""
    print(f"=== {config.name} Docs Scraper ===\n")

    start = time.monotonic()

    print("--- HPC Documentation Pages ---")
    results = scrape_html_sources(config.html_sources, config.keywords)

    print("\n--- Stack Exchange ---")
    results += scrape_se_sources(config.se_sources, config.keywords)

    if not results:
        print("\nNo results collected. Check network access or source URLs.")
        return

    results, duplicates_removed = dedupe_across_sources(results)
    if duplicates_removed:
        print(f"\nRemoved {duplicates_removed} duplicate passage(s) shared across sources.")

    if not results:
        print("\nNo results remain after deduplication.")
        return

    scrape_elapsed = time.monotonic() - start

    if skip_summary:
        print("\n--- Skipping Ollama summarization (--skip-summary) ---")
    else:
        summarize_results(results, model=model, timeout=summary_timeout)

    save_results(results, config.output_path)
    total_passages = sum(len(r["passages"]) for r in results)
    total_elapsed = time.monotonic() - start
    print(f"Total passages collected: {total_passages}")
    print(f"Scrape+dedup time: {scrape_elapsed:.1f}s, total time: {total_elapsed:.1f}s")


def main() -> None:
    args = parse_args()

    if args.list_configs:
        list_configs(CONFIG_DIR)
    else:
        try:
            if args.config:
                config = load_toml_config(Path(args.config))
            else:
                config = run_wizard()

            run_scrape(
                config,
                model=args.model,
                summary_timeout=args.summary_timeout,
                skip_summary=args.skip_summary,
            )
        except ConfigError as e:
            print(f"\nConfig problem: {e}")
        except KeyboardInterrupt:
            print("\nCancelled.")

    # If launched by double-clicking rather than from an already-open
    # terminal, Windows closes the console the instant the script exits
    # the results flash by before anyone can read them. Pausing here keeps
    # the window open. Only do this when stdin is a real interactive
    # terminal, so automated/piped runs (CI, scripts) never hang waiting
    # for a keypress that will never come.
    if sys.stdin.isatty():
        try:
            input("\nPress Enter to exit...")
        except EOFError:
            # Some terminal environments report isatty() as True without
            # actually having readable stdin attached. Don't crash on exit
            # just because the pause couldn't be shown.
            pass


if __name__ == "__main__":
    main()
