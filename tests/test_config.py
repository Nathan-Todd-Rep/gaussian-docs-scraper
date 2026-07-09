from __future__ import annotations

import textwrap
from pathlib import Path

import pytest

from gaussian_scraper.config import (
    ConfigError,
    ScraperConfig,
    load_toml_config,
    save_toml_config,
)


# --- helpers ---

def _valid_config(**overrides) -> ScraperConfig:
    """Return a minimal valid ScraperConfig, with optional field overrides."""
    defaults = dict(
        name="gaussian",
        keywords=["gaussian", "g16"],
        html_sources=[{"label": "Harvard RC", "url": "https://example.com"}],
        se_sources=[],
    )
    defaults.update(overrides)
    return ScraperConfig(**defaults)


# --- validation: name ---

def test_valid_config_passes_validation():
    config = _valid_config()
    assert config.validate() is config


def test_config_rejects_empty_name():
    with pytest.raises(ConfigError, match="name cannot be empty"):
        _valid_config(name="").validate()


def test_config_rejects_name_with_spaces():
    with pytest.raises(ConfigError, match="lowercase with no spaces"):
        _valid_config(name="bio informatics").validate()


def test_config_rejects_uppercase_name():
    with pytest.raises(ConfigError, match="lowercase with no spaces"):
        _valid_config(name="Gaussian").validate()


# --- validation: keywords ---

def test_config_rejects_empty_keywords():
    with pytest.raises(ConfigError, match="At least one keyword"):
        _valid_config(keywords=[]).validate()


# --- validation: sources ---

def test_config_rejects_no_sources():
    with pytest.raises(ConfigError, match="At least one source"):
        _valid_config(html_sources=[], se_sources=[]).validate()


def test_config_rejects_html_source_missing_url():
    with pytest.raises(ConfigError, match="missing required field 'url'"):
        _valid_config(html_sources=[{"label": "No URL"}]).validate()


def test_config_rejects_html_source_missing_label():
    with pytest.raises(ConfigError, match="missing required field 'label'"):
        _valid_config(html_sources=[{"url": "https://example.com"}]).validate()


def test_config_rejects_se_source_missing_tag():
    with pytest.raises(ConfigError, match="missing required field 'tag'"):
        _valid_config(
            html_sources=[],
            se_sources=[{"site": "mattermodeling", "label": "No Tag"}],
        ).validate()


def test_config_rejects_se_source_missing_label():
    with pytest.raises(ConfigError, match="missing required field 'label'"):
        _valid_config(
            html_sources=[],
            se_sources=[{"site": "mattermodeling", "tag": "gaussian"}],
        ).validate()


# --- output path ---

def test_config_default_output_path():
    config = _valid_config()
    expected = Path.home() / ".inkly" / "gaussian_docs.json"
    assert config.output_path == expected


def test_config_custom_output_path():
    custom = Path("/tmp/my_docs.json")
    config = _valid_config(output_path=custom)
    assert config.output_path == custom


# --- TOML loader ---

def test_load_toml_config_happy_path(tmp_path):
    toml_file = tmp_path / "gaussian.toml"
    toml_file.write_text(textwrap.dedent("""
        name = "gaussian"
        keywords = ["gaussian", "g16", "dft"]

        [[html_sources]]
        label = "Harvard RC - Gaussian"
        url = "https://docs.rc.fas.harvard.edu/kb/gaussian/"

        [[se_sources]]
        label = "Matter Modeling SE - gaussian"
        site = "mattermodeling"
        tag = "gaussian"
    """), encoding="utf-8")

    config = load_toml_config(toml_file)

    assert config.name == "gaussian"
    assert "gaussian" in config.keywords
    assert len(config.html_sources) == 1
    assert len(config.se_sources) == 1
    assert config.output_path == Path.home() / ".inkly" / "gaussian_docs.json"


def test_load_toml_config_missing_file(tmp_path):
    with pytest.raises(ConfigError, match="not found"):
        load_toml_config(tmp_path / "nonexistent.toml")


def test_load_toml_config_missing_name(tmp_path):
    toml_file = tmp_path / "bad.toml"
    toml_file.write_text('keywords = ["gaussian"]\n', encoding="utf-8")

    with pytest.raises(ConfigError, match="missing required field 'name'"):
        load_toml_config(toml_file)


def test_load_toml_config_missing_keywords(tmp_path):
    toml_file = tmp_path / "bad.toml"
    toml_file.write_text('name = "gaussian"\n', encoding="utf-8")

    with pytest.raises(ConfigError, match="missing required field 'keywords'"):
        load_toml_config(toml_file)


def test_load_toml_config_custom_output_path(tmp_path):
    toml_file = tmp_path / "gaussian.toml"
    toml_file.write_text(textwrap.dedent("""
        name = "gaussian"
        keywords = ["gaussian"]
        output_path = "/tmp/custom_docs.json"

        [[html_sources]]
        label = "Harvard RC"
        url = "https://example.com"
    """), encoding="utf-8")

    config = load_toml_config(toml_file)

    assert config.output_path == Path("/tmp/custom_docs.json")


# --- save_toml_config ---

def test_save_toml_config_round_trips(tmp_path):
    config = _valid_config(
        name="gaussian",
        keywords=["gaussian", "g16"],
        html_sources=[{"label": "Harvard RC", "url": "https://example.com"}],
        se_sources=[{"label": "MM SE - gaussian", "site": "mattermodeling", "tag": "gaussian"}],
    )

    save_path = tmp_path / "gaussian.toml"
    save_toml_config(config, save_path)

    assert save_path.exists()

    reloaded = load_toml_config(save_path)

    assert reloaded.name == config.name
    assert reloaded.keywords == config.keywords
    assert reloaded.html_sources == config.html_sources
    assert reloaded.se_sources == config.se_sources
    assert reloaded.output_path == config.output_path


def test_save_toml_config_creates_parent_directories(tmp_path):
    config = _valid_config()
    save_path = tmp_path / "nested" / "dir" / "gaussian.toml"

    save_toml_config(config, save_path)

    assert save_path.exists()


def test_save_toml_config_escapes_special_characters(tmp_path):
    config = _valid_config(
        html_sources=[{"label": 'Harvard "RC"', "url": "https://example.com"}],
    )
    save_path = tmp_path / "gaussian.toml"

    save_toml_config(config, save_path)
    reloaded = load_toml_config(save_path)

    assert reloaded.html_sources[0]["label"] == 'Harvard "RC"'
