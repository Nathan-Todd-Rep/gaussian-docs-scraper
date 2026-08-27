from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

try:
    import tomllib  # Python 3.11+
except ModuleNotFoundError:
    import tomli as tomllib  # Python <= 3.10

DEFAULT_OUTPUT_DIR = Path.home() / ".inkly"


class ConfigError(Exception):
    """Raised when a scraper config is invalid or incomplete."""


@dataclass
class ScraperConfig:
    """
    Domain-agnostic configuration for a single scrape run.

    A config defines what to scrape (sources), what to keep (keywords),
    and where to save the output. It can be built by the interactive wizard
    or loaded from a TOML file.

    Attributes:
        name:         Short identifier for the domain (e.g. "gaussian").
                      Must be lowercase with no spaces -- used in the output filename.
        keywords:     List of keywords used to filter passages. A passage must
                      contain at least one keyword to be kept.
        html_sources: List of {label, url} dicts for HTML pages to scrape.
        se_sources:   List of {site, tag, label} dicts for Stack Exchange sources.
        output_path:  Path to the domain's SQLite database file. Defaults to
                      ~/.inkly/{name}.db.
    """

    name: str
    keywords: list[str]
    html_sources: list[dict] = field(default_factory=list)
    se_sources: list[dict] = field(default_factory=list)
    output_path: Path = field(default=None)

    def __post_init__(self):
        if self.output_path is None:
            self.output_path = DEFAULT_OUTPUT_DIR / f"{self.name}.db"
        self.output_path = Path(self.output_path)

    def validate(self) -> "ScraperConfig":
        """
        Validate the config and raise ConfigError if anything is wrong.

        Checks:
        - name is non-empty, lowercase, and contains no spaces
        - at least one keyword is provided
        - at least one source (html or SE) is provided
        - each html_source has label and url
        - each se_source has site, tag, and label

        Returns self so validation can be chained on construction.
        """
        if not self.name or not self.name.strip():
            raise ConfigError("Config name cannot be empty.")

        if not re.match(r"^[a-z0-9_-]+$", self.name):
            raise ConfigError(
                f"Config name must be lowercase with no spaces. "
                f"Got: '{self.name}'. Try '{self.name.lower().replace(' ', '_')}' instead."
            )

        if not self.keywords:
            raise ConfigError("At least one keyword must be provided.")

        if not self.html_sources and not self.se_sources:
            raise ConfigError("At least one source (html_sources or se_sources) must be provided.")

        for i, source in enumerate(self.html_sources):
            if "label" not in source:
                raise ConfigError(f"html_sources[{i}] is missing required field 'label'.")
            if "url" not in source:
                raise ConfigError(f"html_sources[{i}] is missing required field 'url'.")

        for i, source in enumerate(self.se_sources):
            if "site" not in source:
                raise ConfigError(f"se_sources[{i}] is missing required field 'site'.")
            if "tag" not in source:
                raise ConfigError(f"se_sources[{i}] is missing required field 'tag'.")
            if "label" not in source:
                raise ConfigError(f"se_sources[{i}] is missing required field 'label'.")

        if self.output_path.suffix == ".json":
            raise ConfigError(
                f"output_path '{self.output_path}' still points at a .json file. "
                f"Storage is now SQLite-based -- update output_path in your TOML "
                f"config to end in .db (e.g. '{self.output_path.with_suffix('.db')}')."
            )

        return self


def load_toml_config(path: Path) -> ScraperConfig:
    """
    Load and validate a ScraperConfig from a TOML file.

    Expected TOML format:

        name = "gaussian"
        keywords = ["gaussian", "g16", "dft"]

        [[html_sources]]
        label = "Harvard RC - Gaussian"
        url = "https://docs.rc.fas.harvard.edu/kb/gaussian/"

        [[se_sources]]
        label = "Matter Modeling SE - gaussian"
        site = "mattermodeling"
        tag = "gaussian"

    Raises ConfigError if the file is missing, malformed, or invalid.
    """
    if not path.exists():
        raise ConfigError(f"Config file not found: {path}")

    try:
        with path.open("rb") as f:
            raw = tomllib.load(f)
    except Exception as e:
        raise ConfigError(f"Failed to parse TOML config: {e}")

    if "name" not in raw:
        raise ConfigError("Config file is missing required field 'name'.")
    if "keywords" not in raw:
        raise ConfigError("Config file is missing required field 'keywords'.")

    output_path = raw.get("output_path")

    return ScraperConfig(
        name=raw["name"],
        keywords=raw["keywords"],
        html_sources=raw.get("html_sources", []),
        se_sources=raw.get("se_sources", []),
        output_path=Path(output_path) if output_path else None,
    ).validate()


def _toml_string(value: str) -> str:
    """Escape and quote a string for TOML output."""
    escaped = value.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'


def _toml_string_array(values: list[str]) -> str:
    return "[" + ", ".join(_toml_string(v) for v in values) + "]"


def save_toml_config(config: ScraperConfig, path: Path) -> None:
    """
    Write a ScraperConfig out to a TOML file, so it can be reloaded later
    with load_toml_config() or edited by hand.

    The stdlib's tomllib is read-only, so this is a small hand-rolled
    serializer scoped to ScraperConfig's simple shape (strings, string
    lists, and lists of flat string-keyed dicts) rather than a general
    TOML writer.

    Creates parent directories if they do not exist.
    """
    lines = [
        f"name = {_toml_string(config.name)}",
        f"keywords = {_toml_string_array(config.keywords)}",
        f"output_path = {_toml_string(str(config.output_path))}",
    ]

    for source in config.html_sources:
        lines.append("")
        lines.append("[[html_sources]]")
        lines.append(f"label = {_toml_string(source['label'])}")
        lines.append(f"url = {_toml_string(source['url'])}")
        if source.get("tool"):
            lines.append(f"tool = {_toml_string(source['tool'])}")

    for source in config.se_sources:
        lines.append("")
        lines.append("[[se_sources]]")
        lines.append(f"label = {_toml_string(source['label'])}")
        lines.append(f"site = {_toml_string(source['site'])}")
        lines.append(f"tag = {_toml_string(source['tag'])}")
        if source.get("tool"):
            lines.append(f"tool = {_toml_string(source['tool'])}")

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
