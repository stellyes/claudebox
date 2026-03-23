"""
SQLite persistence layer for Claude's creative workspace.
Stores research notes, creative artifacts, and AWS proposals.
"""

import sqlite3
import json
import os
from datetime import datetime, timezone
from pathlib import Path

DB_DIR = Path.home() / ".claude-creative"
DB_PATH = DB_DIR / "workspace.db"


def get_connection() -> sqlite3.Connection:
    DB_DIR.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(DB_PATH))
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL")
    return conn


def init_db():
    conn = get_connection()
    conn.executescript("""
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            tags TEXT DEFAULT '[]',
            source_url TEXT,
            created_at TEXT NOT NULL,
            updated_at TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS artifacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            artifact_type TEXT NOT NULL,
            content TEXT NOT NULL,
            description TEXT,
            tags TEXT DEFAULT '[]',
            created_at TEXT NOT NULL,
            updated_at TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS aws_proposals (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            summary TEXT NOT NULL,
            services TEXT NOT NULL,
            estimated_monthly_cost TEXT,
            architecture TEXT NOT NULL,
            rationale TEXT NOT NULL,
            status TEXT DEFAULT 'pending',
            user_feedback TEXT,
            created_at TEXT NOT NULL,
            updated_at TEXT NOT NULL
        );

        CREATE VIRTUAL TABLE IF NOT EXISTS notes_fts USING fts5(
            title, content, tags, content='notes', content_rowid='id'
        );

        CREATE VIRTUAL TABLE IF NOT EXISTS artifacts_fts USING fts5(
            title, content, description, tags, content='artifacts', content_rowid='id'
        );

        -- Triggers to keep FTS in sync
        CREATE TRIGGER IF NOT EXISTS notes_ai AFTER INSERT ON notes BEGIN
            INSERT INTO notes_fts(rowid, title, content, tags)
            VALUES (new.id, new.title, new.content, new.tags);
        END;

        CREATE TRIGGER IF NOT EXISTS notes_au AFTER UPDATE ON notes BEGIN
            DELETE FROM notes_fts WHERE rowid = old.id;
            INSERT INTO notes_fts(rowid, title, content, tags)
            VALUES (new.id, new.title, new.content, new.tags);
        END;

        CREATE TRIGGER IF NOT EXISTS notes_ad AFTER DELETE ON notes BEGIN
            DELETE FROM notes_fts WHERE rowid = old.id;
        END;

        CREATE TRIGGER IF NOT EXISTS artifacts_ai AFTER INSERT ON artifacts BEGIN
            INSERT INTO artifacts_fts(rowid, title, content, description, tags)
            VALUES (new.id, new.title, new.content, new.description, new.tags);
        END;

        CREATE TRIGGER IF NOT EXISTS artifacts_au AFTER UPDATE ON artifacts BEGIN
            DELETE FROM artifacts_fts WHERE rowid = old.id;
            INSERT INTO artifacts_fts(rowid, title, content, description, tags)
            VALUES (new.id, new.title, new.content, new.description, new.tags);
        END;

        CREATE TRIGGER IF NOT EXISTS artifacts_ad AFTER DELETE ON artifacts BEGIN
            DELETE FROM artifacts_fts WHERE rowid = old.id;
        END;
    """)
    conn.commit()
    conn.close()


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


# ── Notes ──────────────────────────────────────────────────────────────

def save_note(title: str, content: str, tags: list[str] | None = None, source_url: str | None = None) -> dict:
    conn = get_connection()
    now = _now()
    cursor = conn.execute(
        "INSERT INTO notes (title, content, tags, source_url, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?)",
        (title, content, json.dumps(tags or []), source_url, now, now)
    )
    note_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return {"id": note_id, "title": title, "created_at": now}


def search_notes(query: str, limit: int = 10) -> list[dict]:
    conn = get_connection()
    rows = conn.execute(
        "SELECT n.* FROM notes n JOIN notes_fts f ON n.id = f.rowid WHERE notes_fts MATCH ? ORDER BY rank LIMIT ?",
        (query, limit)
    ).fetchall()
    conn.close()
    return [dict(r) for r in rows]


def list_notes(tag: str | None = None, limit: int = 20) -> list[dict]:
    conn = get_connection()
    if tag:
        rows = conn.execute(
            "SELECT id, title, tags, source_url, created_at FROM notes WHERE tags LIKE ? ORDER BY created_at DESC LIMIT ?",
            (f'%"{tag}"%', limit)
        ).fetchall()
    else:
        rows = conn.execute(
            "SELECT id, title, tags, source_url, created_at FROM notes ORDER BY created_at DESC LIMIT ?",
            (limit,)
        ).fetchall()
    conn.close()
    return [dict(r) for r in rows]


def get_note(note_id: int) -> dict | None:
    conn = get_connection()
    row = conn.execute("SELECT * FROM notes WHERE id = ?", (note_id,)).fetchone()
    conn.close()
    return dict(row) if row else None


def delete_note(note_id: int) -> bool:
    conn = get_connection()
    cursor = conn.execute("DELETE FROM notes WHERE id = ?", (note_id,))
    conn.commit()
    conn.close()
    return cursor.rowcount > 0


# ── Artifacts ──────────────────────────────────────────────────────────

def save_artifact(title: str, artifact_type: str, content: str, description: str | None = None, tags: list[str] | None = None) -> dict:
    conn = get_connection()
    now = _now()
    cursor = conn.execute(
        "INSERT INTO artifacts (title, artifact_type, content, description, tags, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?, ?)",
        (title, artifact_type, content, description, json.dumps(tags or []), now, now)
    )
    artifact_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return {"id": artifact_id, "title": title, "type": artifact_type, "created_at": now}


def search_artifacts(query: str, limit: int = 10) -> list[dict]:
    conn = get_connection()
    rows = conn.execute(
        "SELECT a.* FROM artifacts a JOIN artifacts_fts f ON a.id = f.rowid WHERE artifacts_fts MATCH ? ORDER BY rank LIMIT ?",
        (query, limit)
    ).fetchall()
    conn.close()
    return [dict(r) for r in rows]


def list_artifacts(artifact_type: str | None = None, limit: int = 20) -> list[dict]:
    conn = get_connection()
    if artifact_type:
        rows = conn.execute(
            "SELECT id, title, artifact_type, description, tags, created_at FROM artifacts WHERE artifact_type = ? ORDER BY created_at DESC LIMIT ?",
            (artifact_type, limit)
        ).fetchall()
    else:
        rows = conn.execute(
            "SELECT id, title, artifact_type, description, tags, created_at FROM artifacts ORDER BY created_at DESC LIMIT ?",
            (limit,)
        ).fetchall()
    conn.close()
    return [dict(r) for r in rows]


def get_artifact(artifact_id: int) -> dict | None:
    conn = get_connection()
    row = conn.execute("SELECT * FROM artifacts WHERE id = ?", (artifact_id,)).fetchone()
    conn.close()
    return dict(row) if row else None


def update_artifact(artifact_id: int, content: str, description: str | None = None) -> bool:
    conn = get_connection()
    now = _now()
    if description:
        cursor = conn.execute(
            "UPDATE artifacts SET content = ?, description = ?, updated_at = ? WHERE id = ?",
            (content, description, now, artifact_id)
        )
    else:
        cursor = conn.execute(
            "UPDATE artifacts SET content = ?, updated_at = ? WHERE id = ?",
            (content, now, artifact_id)
        )
    conn.commit()
    conn.close()
    return cursor.rowcount > 0


def delete_artifact(artifact_id: int) -> bool:
    conn = get_connection()
    cursor = conn.execute("DELETE FROM artifacts WHERE id = ?", (artifact_id,))
    conn.commit()
    conn.close()
    return cursor.rowcount > 0


# ── AWS Proposals ──────────────────────────────────────────────────────

def save_proposal(title: str, summary: str, services: list[str], estimated_monthly_cost: str, architecture: str, rationale: str) -> dict:
    conn = get_connection()
    now = _now()
    cursor = conn.execute(
        "INSERT INTO aws_proposals (title, summary, services, estimated_monthly_cost, architecture, rationale, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
        (title, summary, json.dumps(services), estimated_monthly_cost, architecture, rationale, now, now)
    )
    proposal_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return {"id": proposal_id, "title": title, "status": "pending", "created_at": now}


def list_proposals(status: str | None = None, limit: int = 20) -> list[dict]:
    conn = get_connection()
    if status:
        rows = conn.execute(
            "SELECT id, title, summary, estimated_monthly_cost, status, created_at FROM aws_proposals WHERE status = ? ORDER BY created_at DESC LIMIT ?",
            (status, limit)
        ).fetchall()
    else:
        rows = conn.execute(
            "SELECT id, title, summary, estimated_monthly_cost, status, created_at FROM aws_proposals ORDER BY created_at DESC LIMIT ?",
            (limit,)
        ).fetchall()
    conn.close()
    return [dict(r) for r in rows]


def get_proposal(proposal_id: int) -> dict | None:
    conn = get_connection()
    row = conn.execute("SELECT * FROM aws_proposals WHERE id = ?", (proposal_id,)).fetchone()
    conn.close()
    return dict(row) if row else None


def update_proposal_status(proposal_id: int, status: str, feedback: str | None = None) -> bool:
    conn = get_connection()
    now = _now()
    cursor = conn.execute(
        "UPDATE aws_proposals SET status = ?, user_feedback = ?, updated_at = ? WHERE id = ?",
        (status, feedback, now, proposal_id)
    )
    conn.commit()
    conn.close()
    return cursor.rowcount > 0


# ── Stats ──────────────────────────────────────────────────────────────

def workspace_stats() -> dict:
    conn = get_connection()
    notes_count = conn.execute("SELECT COUNT(*) FROM notes").fetchone()[0]
    artifacts_count = conn.execute("SELECT COUNT(*) FROM artifacts").fetchone()[0]
    proposals_count = conn.execute("SELECT COUNT(*) FROM aws_proposals").fetchone()[0]
    pending_proposals = conn.execute("SELECT COUNT(*) FROM aws_proposals WHERE status = 'pending'").fetchone()[0]
    conn.close()
    return {
        "notes": notes_count,
        "artifacts": artifacts_count,
        "proposals_total": proposals_count,
        "proposals_pending": pending_proposals,
        "db_path": str(DB_PATH),
    }
