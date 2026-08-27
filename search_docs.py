#!/usr/bin/env python3
"""
Search a domain's scraped passages by relevance instead of dumping all of
them.

Ranks passages already collected by scrape.py against a query using TF-IDF
+ cosine similarity, so a consumer only needs the top few relevant
passages -- not the entire scraped dataset -- to answer one question.

Usage:

    py search_docs.py --domain gaussian --query "how do I set memory for a job?"
    py search_docs.py --domain bioinformatics --query "align reads with bwa" --top-k 3
"""
from __future__ import annotations

import argparse

from gaussian_scraper.passage_index import PassageIndex


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Search a domain's scraped passages by relevance to a query."
    )
    parser.add_argument("--domain", required=True, help="Domain name, e.g. 'gaussian'.")
    parser.add_argument("--query", required=True, help="Question to rank passages against.")
    parser.add_argument(
        "--top-k",
        type=int,
        default=5,
        help="Maximum number of passages to return (default: 5).",
    )
    parser.add_argument(
        "--tool",
        type=str,
        default=None,
        help="Only search passages from sources tagged with this tool (e.g. 'samtools'). "
             "Only meaningful for domains that tag sources by tool.",
    )
    return parser.parse_args()


def print_matches(matches: list) -> None:
    if not matches or matches[0].score <= 0.0:
        print("No relevant passages found -- query shares no vocabulary with this domain's data.")
        return

    for i, match in enumerate(matches, start=1):
        if match.score <= 0.0:
            break
        print(f"\n{i}. [{match.label}] (score: {match.score:.3f})")
        print(f"   {match.text}")


def main() -> None:
    args = parse_args()

    try:
        index = PassageIndex.load(args.domain)
    except FileNotFoundError as e:
        raise SystemExit(str(e))

    matches = index.search(args.query, top_k=args.top_k, tool=args.tool)
    print_matches(matches)


if __name__ == "__main__":
    main()
