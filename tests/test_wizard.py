from __future__ import annotations

from gaussian_scraper import wizard
from gaussian_scraper.presets import GAUSSIAN_PRESET
from gaussian_scraper.wizard import parse_selection, run_wizard, sanitize_name


# --- sanitize_name ---

def test_sanitize_name_lowercases_and_replaces_spaces():
    assert sanitize_name("Bio Informatics") == "bio_informatics"


def test_sanitize_name_collapses_camel_case():
    assert sanitize_name("BioInformatics") == "bioinformatics"


def test_sanitize_name_strips_whitespace():
    assert sanitize_name("  gaussian  ") == "gaussian"


def test_sanitize_name_replaces_invalid_characters():
    assert sanitize_name("Bio-Informatics!") == "bio-informatics"


def test_sanitize_name_returns_empty_for_blank_input():
    assert sanitize_name("   ") == ""


# --- parse_selection ---

def test_parse_selection_basic():
    assert parse_selection("1,3", 5) == [0, 2]


def test_parse_selection_handles_spaces():
    assert parse_selection(" 2 , 4 ", 5) == [1, 3]


def test_parse_selection_returns_empty_for_blank_input():
    assert parse_selection("", 5) == []
    assert parse_selection("   ", 5) == []


def test_parse_selection_ignores_non_numeric_input():
    assert parse_selection("abc", 5) == []


def test_parse_selection_ignores_out_of_range_values():
    assert parse_selection("1,99", 5) == [0]


# --- run_wizard: preset flow ---

def _fake_io(inputs: list[str]):
    """Return (input_func, print_func, printed_lines) for driving the wizard."""
    iterator = iter(inputs)
    printed = []

    def input_func(prompt):
        return next(iterator)

    def print_func(*args, **kwargs):
        printed.append(" ".join(str(a) for a in args))

    return input_func, print_func, printed


def test_wizard_preset_flow_uses_defaults(monkeypatch):
    monkeypatch.setattr(wizard, "discover_se_tags", lambda topic, sites=None: [])

    input_func, print_func, _ = _fake_io(["1", "", "n", "n"])

    config = run_wizard(input_func=input_func, print_func=print_func)

    assert config.name == "gaussian"
    assert config.keywords == GAUSSIAN_PRESET["keywords"]
    assert len(config.html_sources) == len(GAUSSIAN_PRESET["html_sources"])
    assert len(config.se_sources) == len(GAUSSIAN_PRESET["se_sources"])


def test_wizard_preset_flow_accepts_custom_keywords(monkeypatch):
    monkeypatch.setattr(wizard, "discover_se_tags", lambda topic, sites=None: [])

    input_func, print_func, _ = _fake_io(["1", "custom, keywords, here", "n", "n"])

    config = run_wizard(input_func=input_func, print_func=print_func)

    assert config.keywords == ["custom", "keywords", "here"]


# --- run_wizard: custom topic flow ---

def test_wizard_custom_topic_flow(monkeypatch):
    fake_tags = [
        {"site": "bioinformatics", "tag": "rna-seq", "count": 717, "label": "bioinformatics - rna-seq"},
    ]
    monkeypatch.setattr(wizard, "discover_se_tags", lambda topic, sites=None: fake_tags)

    inputs = [
        "3",                        # custom topic (option after the 2 presets)
        "Bio Informatics",          # topic
        "1",                        # select the discovered tag
        "y",                        # add a website
        "https://example.com",      # url
        "Example",                  # label
        "n",                        # stop adding websites
        "rna-seq, fastq",           # keywords
        "n",                        # decline save
    ]
    input_func, print_func, _ = _fake_io(inputs)

    config = run_wizard(input_func=input_func, print_func=print_func)

    assert config.name == "bio_informatics"
    assert config.keywords == ["rna-seq", "fastq"]
    assert config.html_sources == [{"label": "Example", "url": "https://example.com"}]
    assert config.se_sources == [
        {"label": "bioinformatics - rna-seq", "site": "bioinformatics", "tag": "rna-seq"}
    ]


def test_wizard_retries_when_no_keywords_entered(monkeypatch):
    monkeypatch.setattr(wizard, "discover_se_tags", lambda topic, sites=None: [])

    inputs = [
        "3",                        # custom topic
        "gaussian",                 # topic
        "y",                        # add a website
        "https://example.com",
        "Ex",
        "n",                        # stop adding websites
        "",                         # blank keywords (first attempt)
        "gaussian, dft",            # keywords (retry)
        "n",                        # decline save
    ]
    input_func, print_func, printed = _fake_io(inputs)

    config = run_wizard(input_func=input_func, print_func=print_func)

    assert config.keywords == ["gaussian", "dft"]
    assert any("At least one keyword is required" in line for line in printed)


def test_wizard_retries_when_no_sources_selected(monkeypatch):
    monkeypatch.setattr(wizard, "discover_se_tags", lambda topic, sites=None: [])

    inputs = [
        "3",                        # custom topic
        "gaussian",                 # topic
        "n",                        # no websites (first round)
        "gaussian, dft",            # keywords
        "y",                        # retry round: add a website
        "https://example.com",
        "Ex",
        "n",                        # stop adding
        "n",                        # decline save
    ]
    input_func, print_func, printed = _fake_io(inputs)

    config = run_wizard(input_func=input_func, print_func=print_func)

    assert len(config.html_sources) == 1
    assert any("No sources selected" in line for line in printed)


# --- run_wizard: save prompt ---

def test_wizard_saves_config_when_requested(monkeypatch, tmp_path):
    monkeypatch.setattr(wizard, "discover_se_tags", lambda topic, sites=None: [])

    save_path = tmp_path / "gaussian.toml"
    inputs = ["1", "", "n", "y", str(save_path)]
    input_func, print_func, printed = _fake_io(inputs)

    config = run_wizard(input_func=input_func, print_func=print_func)

    assert save_path.exists()
    assert any("Saved config" in line for line in printed)

    saved_text = save_path.read_text(encoding="utf-8")
    assert 'name = "gaussian"' in saved_text


def test_wizard_skips_save_when_declined(monkeypatch, tmp_path):
    monkeypatch.setattr(wizard, "discover_se_tags", lambda topic, sites=None: [])
    monkeypatch.setattr(wizard, "DEFAULT_CONFIG_DIR", tmp_path)

    inputs = ["1", "", "n", "n"]
    input_func, print_func, printed = _fake_io(inputs)

    run_wizard(input_func=input_func, print_func=print_func)

    assert not any("Saved config" in line for line in printed)
    assert list(tmp_path.iterdir()) == []


def test_wizard_save_uses_default_path_when_blank(monkeypatch, tmp_path):
    monkeypatch.setattr(wizard, "discover_se_tags", lambda topic, sites=None: [])
    monkeypatch.setattr(wizard, "DEFAULT_CONFIG_DIR", tmp_path)

    inputs = ["1", "", "n", "y", ""]
    input_func, print_func, printed = _fake_io(inputs)

    run_wizard(input_func=input_func, print_func=print_func)

    assert (tmp_path / "gaussian.toml").exists()
