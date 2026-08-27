from __future__ import annotations

import hashlib
import sqlite3
from datetime import datetime, timezone
from pathlib import Path

_SCHEMA = """
CREATE TABLE IF NOT EXISTS sources (
    id              INTEGER PRIMARY KEY,
    label           TEXT NOT NULL UNIQUE,
    source_type     TEXT NOT NULL CHECK (source_type IN ('html', 'se')),
    url             TEXT,
    site            TEXT,
    tag             TEXT,
    tool            TEXT,
    content_hash    TEXT NOT NULL,
    summary         TEXT,
    last_scraped_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS passages (
    id        INTEGER PRIMARY KEY,
    source_id INTEGER NOT NULL REFERENCES sources(id) ON DELETE CASCADE,
    position  INTEGER NOT NULL,
    text      TEXT NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_passages_source_id ON passages(source_id);
"""


def _ensure_tool_column(conn: sqlite3.Connection) -> None:
    """
    Add the tool column to a database created before it existed.

    CREATE TABLE IF NOT EXISTS is a no-op against an already-existing
    sources table, so a DB created before this column existed needs an
    explicit ALTER TABLE to catch up without losing its existing rows.
    """
    columns = [row[1] for row in conn.execute("PRAGMA table_info(sources)").fetchall()]
    if "tool" not in columns:
        conn.execute("ALTER TABLE sources ADD COLUMN tool TEXT")


def _connect(db_path: Path) -> sqlite3.Connection:
    """Open a connection with foreign keys enabled, creating the parent dir if needed."""
    db_path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(db_path)
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def init_db(db_path: Path) -> None:
    """Create the sources/passages tables if they don't already exist. Idempotent."""
    conn = _connect(db_path)
    try:
        conn.executescript(_SCHEMA)
        _ensure_tool_column(conn)
        conn.commit()
    finally:
        conn.close()


def compute_content_hash(passages: list[str]) -> str:
    """
    Sha256 of the passages, sorted then newline-joined, so the hash is
    independent of extraction/dedup ordering -- nondeterministic ordering
    across runs shouldn't register as a content change.
    """
    joined = "\n".join(sorted(passages))
    return hashlib.sha256(joined.encode("utf-8")).hexdigest()


def _infer_source_type(result: dict) -> str:
    return "html" if "url" in result else "se"


def save_results(results: list[dict], db_path: Path) -> None:
    """
    Replace this domain's entire dataset with `results`, atomically.

    Wipes all existing sources/passages in db_path and re-inserts the
    current run's results in a single transaction. This mirrors the old
    JSON behavior: save_results always overwrote the whole file, so a
    source that failed to fetch this run simply disappears from the
    dataset until it succeeds again.
    """
    init_db(db_path)
    conn = _connect(db_path)
    try:
        conn.execute("DELETE FROM sources")

        now = datetime.now(timezone.utc).isoformat()
        for result in results:
            source_type = _infer_source_type(result)
            content_hash = compute_content_hash(result["passages"])
            cursor = conn.execute(
                """
                INSERT INTO sources (label, source_type, url, site, tag, tool, content_hash, summary, last_scraped_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    result["label"],
                    source_type,
                    result.get("url"),
                    result.get("site"),
                    result.get("tag"),
                    result.get("tool"),
                    content_hash,
                    result.get("summary"),
                    now,
                ),
            )
            source_id = cursor.lastrowid
            conn.executemany(
                "INSERT INTO passages (source_id, position, text) VALUES (?, ?, ?)",
                [(source_id, i, text) for i, text in enumerate(result["passages"])],
            )

        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


def load_domain_records(domain: str, db_path: Path) -> list[dict]:
    """
    Return [{"label": ..., "passages": [...]}, ...] for every source in
    db_path, ordered by insertion order, passages ordered by position.

    Raises FileNotFoundError if db_path doesn't exist or contains zero
    sources, matching the old JSON-file-missing contract that
    PassageIndex.load()/search_docs.py already rely on.
    """
    if not db_path.exists():
        raise FileNotFoundError(f"No scraped data for domain '{domain}' at {db_path}")

    conn = _connect(db_path)
    try:
        rows = conn.execute("SELECT id, label, tool FROM sources ORDER BY id").fetchall()
        if not rows:
            raise FileNotFoundError(f"No scraped data for domain '{domain}' at {db_path}")

        records = []
        for source_id, label, tool in rows:
            passage_rows = conn.execute(
                "SELECT text FROM passages WHERE source_id = ? ORDER BY position",
                (source_id,),
            ).fetchall()
            records.append({
                "label": label,
                "tool": tool,
                "passages": [text for (text,) in passage_rows],
            })

        return records
    finally:
        conn.close()


def get_source_hash_and_summary(label: str, db_path: Path) -> tuple[str, str | None] | None:
    """
    Look up the previously stored (content_hash, summary) for a source by
    label. Returns None if db_path doesn't exist or the label isn't
    present (new source, or first-ever scrape).
    """
    if not db_path.exists():
        return None

    conn = _connect(db_path)
    try:
        row = conn.execute(
            "SELECT content_hash, summary FROM sources WHERE label = ?",
            (label,),
        ).fetchone()
        return tuple(row) if row else None
    finally:
        conn.close()
