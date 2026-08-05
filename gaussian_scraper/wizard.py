from __future__ import annotations

import re
from pathlib import Path
from typing import Callable

from gaussian_scraper.config import ScraperConfig, save_toml_config
from gaussian_scraper.presets import PRESETS
from gaussian_scraper.stackexchange import discover_se_tags

# Directory where wizard-saved configs are offered as the default location.
DEFAULT_CONFIG_DIR = Path("configs")

# Type aliases for injectable I/O, so the wizard's flow logic can be tested
# without touching real stdin/stdout.
InputFunc = Callable[[str], str]
PrintFunc = Callable[..., None]


def sanitize_name(raw: str) -> str:
    """
    Convert free-form user input into a valid ScraperConfig name.

    Lowercases the input, replaces whitespace and invalid characters with
    underscores, and strips leading/trailing underscores. This means users
    never need to know that config names must be lowercase with no spaces --
    "Bio Informatics", "BioInformatics", and "bio-informatics" are all
    normalized automatically.
    """
    lowered = raw.strip().lower()
    normalized = re.sub(r"[^a-z0-9_-]+", "_", lowered)
    return normalized.strip("_")


def parse_selection(raw: str, max_index: int) -> list[int]:
    """
    Parse a comma-separated selection string like "1,3,5" into a list of
    zero-based indices.

    Only in-range values (1..max_index) are kept; anything else is
    silently ignored so a typo doesn't crash the wizard. Returns an empty
    list if raw is blank.
    """
    if not raw or not raw.strip():
        return []

    indices = []
    for part in raw.split(","):
        part = part.strip()
        if not part.isdigit():
            continue
        n = int(part)
        if 1 <= n <= max_index:
            indices.append(n - 1)

    return indices


def _prompt_preset_choice(input_func: InputFunc, print_func: PrintFunc) -> dict | None:
    """
    Show the preset menu and return the chosen preset dict, or None if the
    user chose "Custom topic".
    """
    print_func("What would you like to scrape?")
    for i, preset in enumerate(PRESETS, start=1):
        print_func(f"  {i}. {preset['display_name']}")
    custom_option = len(PRESETS) + 1
    print_func(f"  {custom_option}. Custom topic")

    while True:
        raw = input_func(f"Select an option [1-{custom_option}]: ")
        if raw.strip().isdigit():
            choice = int(raw.strip())
            if 1 <= choice <= len(PRESETS):
                return PRESETS[choice - 1]
            if choice == custom_option:
                return None
        print_func(f"Please enter a number between 1 and {custom_option}.")


def _prompt_se_tags(topic: str, input_func: InputFunc, print_func: PrintFunc) -> list[dict]:
    """
    Discover Stack Exchange tags for the given topic and let the user pick
    which ones to include. Returns a list of se_source dicts.
    """
    print_func(f"\nSearching Stack Exchange for '{topic}' tags...")
    results = discover_se_tags(topic)

    if not results:
        print_func("No matching tags found.")
        return []

    print_func("Found these tags:")
    for i, r in enumerate(results, start=1):
        print_func(f"  {i}. {r['site']} - {r['tag']} ({r['count']} questions)")

    raw = input_func("Select tags to include (e.g. 1,3 or press Enter to skip): ")
    indices = parse_selection(raw, len(results))

    selected = [results[i] for i in indices]
    return [
        {"label": r["label"], "site": r["site"], "tag": r["tag"]}
        for r in selected
    ]


def _prompt_html_sources(input_func: InputFunc, print_func: PrintFunc) -> list[dict]:
    """
    Interactively collect additional HTML sources (label + url pairs) from
    the user. Returns a list of html_source dicts.
    """
    sources = []

    while True:
        add_more = input_func("Add a website URL to scrape? (y/n): ").strip().lower()
        if add_more != "y":
            break

        url = input_func("  URL: ").strip()
        if not url:
            print_func("  Skipped -- no URL entered.")
            continue

        label = input_func("  Label: ").strip()
        if not label:
            label = url

        sources.append({"label": label, "url": url})

    return sources


def _prompt_keywords(default_keywords: list[str], input_func: InputFunc, print_func: PrintFunc) -> list[str]:
    """
    Ask the user for keywords, offering the preset's defaults (if any) as a
    starting point. Returns the final keyword list.
    """
    if default_keywords:
        print_func(f"\nDefault keywords: {', '.join(default_keywords)}")
        raw = input_func(
            "Press Enter to keep these, or type your own comma-separated list: "
        )
        if not raw.strip():
            return default_keywords
        return [kw.strip() for kw in raw.split(",") if kw.strip()]

    raw = input_func("\nEnter keywords to filter passages (comma separated): ")
    return [kw.strip() for kw in raw.split(",") if kw.strip()]


def _prompt_save_config(config: ScraperConfig, input_func: InputFunc, print_func: PrintFunc) -> None:
    """
    Ask the user whether to save the finished config as a TOML file for
    reuse, and write it if so. Failures are reported but never raised --
    a save failure should not lose the config the user just built.
    """
    raw = input_func("\nSave this config as a TOML file for reuse? (y/n): ").strip().lower()
    if raw != "y":
        return

    default_path = DEFAULT_CONFIG_DIR / f"{config.name}.toml"
    raw_path = input_func(f"Save as [{default_path}]: ").strip()
    save_path = Path(raw_path) if raw_path else default_path

    try:
        save_toml_config(config, save_path)
        print_func(f"Saved config to {save_path}")
    except OSError as e:
        print_func(f"Could not save config: {e}")


def run_wizard(
    input_func: InputFunc = input,
    print_func: PrintFunc = print,
) -> ScraperConfig:
    """
    Run the interactive setup wizard and return a validated ScraperConfig.

    Flow:
    1. User picks a built-in preset or "Custom topic".
    2. For a preset: keywords and html_sources are pre-populated from
       curated, validated data. SE tags are re-discovered live so results
       stay current, and the user can add extra tags or URLs on top.
    3. For a custom topic: the user types a topic, SE tags are discovered
       live, and the user builds keywords/sources from scratch.
    4. If the resulting config has no sources at all, the wizard loops back
       to source selection rather than producing an invalid config.
    """
    print_func("Welcome to the Scraper Setup Wizard.\n")

    preset = _prompt_preset_choice(input_func, print_func)

    if preset:
        name = preset["name"]
        topic = preset["name"]
        keywords = _prompt_keywords(preset["keywords"], input_func, print_func)
        html_sources = list(preset["html_sources"])
        se_sources = list(preset["se_sources"])

        print_func("\nWould you like to add any additional sources?")
        se_sources += _prompt_se_tags(topic, input_func, print_func)
        html_sources += _prompt_html_sources(input_func, print_func)
    else:
        raw_topic = input_func("\nWhat topic do you want to scrape? ")
        name = sanitize_name(raw_topic)
        while not name:
            print_func("That topic couldn't be converted to a valid name. Try again.")
            raw_topic = input_func("What topic do you want to scrape? ")
            name = sanitize_name(raw_topic)

        se_sources = _prompt_se_tags(raw_topic.strip(), input_func, print_func)
        html_sources = _prompt_html_sources(input_func, print_func)
        keywords = _prompt_keywords([], input_func, print_func)

    while not keywords:
        print_func("\nAt least one keyword is required so results can be filtered.")
        keywords = _prompt_keywords([], input_func, print_func)

    while not html_sources and not se_sources:
        print_func("\nNo sources selected. Please add at least one tag or URL.")
        se_sources += _prompt_se_tags(name, input_func, print_func)
        html_sources += _prompt_html_sources(input_func, print_func)

    config = ScraperConfig(
        name=name,
        keywords=keywords,
        html_sources=html_sources,
        se_sources=se_sources,
    )
    config.validate()

    print_func(f"\nConfig '{name}' ready: {len(html_sources)} website source(s), "
               f"{len(se_sources)} Stack Exchange source(s), {len(keywords)} keyword(s).")

    _prompt_save_config(config, input_func, print_func)

    return config
