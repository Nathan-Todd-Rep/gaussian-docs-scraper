#!/usr/bin/env python3
"""
Vet candidate HTML sources before adding them to a preset or config.

Replaces manual curl + grep vetting with a repeatable, automated check.
Each URL is fetched and classified as GOOD, WEAK, EMPTY, or FAIL based on
how many lines match the given keywords -- the same bar we've been
applying by hand when building the Gaussian and Bioinformatics presets.

Usage:

    py check_sources.py --config configs/gaussian.toml
        Re-check every html_source already in a saved config.

    py check_sources.py --keywords "gaussian,g16,dft" \\
        --url "https://example.edu/gaussian" --label "Example - Gaussian"
        Check one or more ad-hoc candidate URLs before adding them anywhere.
"""
from __future__ import annotations

import argparse
from pathlib import Path

from gaussian_scraper.config import load_toml_config
from gaussian_scraper.source_check import check_sources

VERDICT_ORDER = ["GOOD", "WEAK", "EMPTY", "FAIL"]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Vet candidate HTML sources.")
    parser.add_argument("--config", type=str, help="Path to a TOML config; checks its html_sources.")
    parser.add_argument("--url", action="append", default=[], help="Ad-hoc URL to check (repeatable).")
    parser.add_argument("--label", action="append", default=[], help="Label for each --url, in order (repeatable).")
    parser.add_argument("--keywords", type=str, help="Comma-separated keywords for ad-hoc URL checks.")
    return parser.parse_args()


def build_sources_and_keywords(args: argparse.Namespace) -> tuple[list[dict], list[str]]:
    if args.config:
        config = load_toml_config(Path(args.config))
        return config.html_sources, config.keywords

    if not args.url:
        raise SystemExit("Provide --config, or at least one --url with --keywords.")
    if not args.keywords:
        raise SystemExit("--keywords is required when checking ad-hoc URLs.")

    keywords = [kw.strip() for kw in args.keywords.split(",") if kw.strip()]
    labels = args.label + [""] * (len(args.url) - len(args.label))
    sources = [
        {"label": label or url, "url": url}
        for url, label in zip(args.url, labels)
    ]
    return sources, keywords


def print_report(results: list[dict]) -> None:
    by_verdict = {v: [r for r in results if r["verdict"] == v] for v in VERDICT_ORDER}

    for verdict in VERDICT_ORDER:
        group = by_verdict[verdict]
        if not group:
            continue
        print(f"\n{verdict} ({len(group)}):")
        for r in group:
            print(f"  {r['label']}")
            print(f"    {r['url']}")
            print(f"    {r['reason']}")

    total = len(results)
    good = len(by_verdict["GOOD"])
    print(f"\n{good}/{total} sources are GOOD.")


def main() -> None:
    args = parse_args()
    sources, keywords = build_sources_and_keywords(args)

    print(f"Checking {len(sources)} source(s) against {len(keywords)} keyword(s)...\n")
    results = check_sources(sources, keywords)
    print_report(results)


if __name__ == "__main__":
    main()
