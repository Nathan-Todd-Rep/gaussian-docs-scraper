from __future__ import annotations

import sqlite3

import pytest

from gaussian_scraper import storage


# --- init_db ---

def test_init_db_creates_expected_tables(tmp_path):
    db_path = tmp_path / "gaussian.db"
    storage.init_db(db_path)

    conn = sqlite3.connect(db_path)
    tables = {
        row[0]
        for row in conn.execute("SELECT name FROM sqlite_master WHERE type='table'")
    }
    conn.close()

    assert {"sources", "passages"} <= tables


def test_init_db_includes_tool_column_on_fresh_db(tmp_path):
    db_path = tmp_path / "gaussian.db"
    storage.init_db(db_path)

    conn = sqlite3.connect(db_path)
    columns = [row[1] for row in conn.execute("PRAGMA table_info(sources)").fetchall()]
    conn.close()

    assert "tool" in columns


def test_init_db_migrates_existing_db_missing_tool_column(tmp_path):
    db_path = tmp_path / "bioinformatics.db"

    # Simulate a DB created before the tool column existed.
    conn = sqlite3.connect(db_path)
    conn.execute("""
        CREATE TABLE sources (
            id              INTEGER PRIMARY KEY,
            label           TEXT NOT NULL UNIQUE,
            source_type     TEXT NOT NULL,
            url             TEXT,
            site            TEXT,
            tag             TEXT,
            content_hash    TEXT NOT NULL,
            summary         TEXT,
            last_scraped_at TEXT NOT NULL
        )
    """)
    conn.execute(
        "INSERT INTO sources (label, source_type, url, content_hash, last_scraped_at) "
        "VALUES ('Old Source', 'html', 'https://example.com', 'abc123', '2026-01-01')"
    )
    conn.commit()
    conn.close()

    storage.init_db(db_path)

    conn = sqlite3.connect(db_path)
    columns = [row[1] for row in conn.execute("PRAGMA table_info(sources)").fetchall()]
    label, tool = conn.execute("SELECT label, tool FROM sources WHERE label = 'Old Source'").fetchone()
    conn.close()

    assert "tool" in columns
    assert label == "Old Source"
    assert tool is None


# --- compute_content_hash ---

def test_compute_content_hash_is_order_independent():
    a = storage.compute_content_hash(["one", "two", "three"])
    b = storage.compute_content_hash(["three", "one", "two"])
    assert a == b


def test_compute_content_hash_changes_when_passages_change():
    a = storage.compute_content_hash(["one", "two"])
    b = storage.compute_content_hash(["one", "two", "three"])
    assert a != b


# --- save_results / load_domain_records ---

def test_save_results_infers_html_source_type(tmp_path):
    db_path = tmp_path / "gaussian.db"
    storage.save_results(
        [{"label": "Harvard RC", "url": "https://example.com", "passages": ["a"]}],
        db_path,
    )

    conn = sqlite3.connect(db_path)
    source_type = conn.execute("SELECT source_type FROM sources WHERE label = 'Harvard RC'").fetchone()[0]
    conn.close()

    assert source_type == "html"


def test_save_results_infers_se_source_type(tmp_path):
    db_path = tmp_path / "gaussian.db"
    storage.save_results(
        [{"label": "MM SE - gaussian", "site": "mattermodeling", "tag": "gaussian", "passages": ["a"]}],
        db_path,
    )

    conn = sqlite3.connect(db_path)
    source_type = conn.execute("SELECT source_type FROM sources WHERE label = 'MM SE - gaussian'").fetchone()[0]
    conn.close()

    assert source_type == "se"


def test_save_results_round_trips_through_load_domain_records(tmp_path):
    db_path = tmp_path / "gaussian.db"
    results = [
        {"label": "Harvard RC", "url": "https://example.com", "passages": ["one", "two"]},
        {"label": "MM SE - gaussian", "site": "mattermodeling", "tag": "gaussian", "passages": ["three"]},
    ]
    storage.save_results(results, db_path)

    records = storage.load_domain_records("gaussian", db_path)

    assert records == [
        {"label": "Harvard RC", "tool": None, "passages": ["one", "two"]},
        {"label": "MM SE - gaussian", "tool": None, "passages": ["three"]},
    ]


def test_save_results_round_trips_tool_field(tmp_path):
    db_path = tmp_path / "bioinformatics.db"
    results = [
        {"label": "Samtools GitHub", "url": "https://github.com/samtools/samtools", "tool": "samtools", "passages": ["one"]},
        {"label": "General Bio Guide", "url": "https://example.com", "passages": ["two"]},
    ]
    storage.save_results(results, db_path)

    records = storage.load_domain_records("bioinformatics", db_path)

    assert records == [
        {"label": "Samtools GitHub", "tool": "samtools", "passages": ["one"]},
        {"label": "General Bio Guide", "tool": None, "passages": ["two"]},
    ]


def test_save_results_preserves_passage_order(tmp_path):
    db_path = tmp_path / "gaussian.db"
    passages = [f"passage {i}" for i in range(10)]
    storage.save_results([{"label": "A", "url": "https://example.com", "passages": passages}], db_path)

    records = storage.load_domain_records("gaussian", db_path)

    assert records[0]["passages"] == passages


def test_save_results_rerun_replaces_domain_without_duplicates(tmp_path):
    db_path = tmp_path / "gaussian.db"
    storage.save_results(
        [
            {"label": "A", "url": "https://example.com", "passages": ["one"]},
            {"label": "B", "url": "https://example.com", "passages": ["two"]},
        ],
        db_path,
    )

    storage.save_results(
        [{"label": "A", "url": "https://example.com", "passages": ["one updated"]}],
        db_path,
    )

    records = storage.load_domain_records("gaussian", db_path)

    assert records == [{"label": "A", "tool": None, "passages": ["one updated"]}]


def test_load_domain_records_raises_when_db_missing(tmp_path):
    with pytest.raises(FileNotFoundError):
        storage.load_domain_records("nonexistent", tmp_path / "missing.db")


def test_load_domain_records_raises_when_domain_has_no_sources(tmp_path):
    db_path = tmp_path / "gaussian.db"
    storage.init_db(db_path)

    with pytest.raises(FileNotFoundError):
        storage.load_domain_records("gaussian", db_path)


# --- get_source_hash_and_summary ---

def test_get_source_hash_and_summary_returns_none_for_unknown_label(tmp_path):
    db_path = tmp_path / "gaussian.db"
    storage.save_results([{"label": "A", "url": "https://example.com", "passages": ["one"]}], db_path)

    assert storage.get_source_hash_and_summary("Unknown", db_path) is None


def test_get_source_hash_and_summary_returns_none_when_db_missing(tmp_path):
    assert storage.get_source_hash_and_summary("A", tmp_path / "missing.db") is None


def test_get_source_hash_and_summary_returns_stored_values_after_save(tmp_path):
    db_path = tmp_path / "gaussian.db"
    storage.save_results(
        [{"label": "A", "url": "https://example.com", "passages": ["one", "two"], "summary": "A summary."}],
        db_path,
    )

    result = storage.get_source_hash_and_summary("A", db_path)

    assert result == (storage.compute_content_hash(["one", "two"]), "A summary.")
