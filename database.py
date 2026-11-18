"""
database.py - SQLite Database Initializer and Persistence Layer
"""
import sqlite3
import json
from pathlib import Path
from schemas import CandidateDossier

DB_PATH = Path(__file__).resolve().parent / "data" / "research_dossiers.db"

def init_db(db_path: Path = DB_PATH):
    db_path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS profiles (
        candidate_id TEXT PRIMARY KEY,
        category_tag TEXT NOT NULL,
        full_name TEXT NOT NULL,
        aliases TEXT,
        nationality_location TEXT,
        birth_year INTEGER,
        current_age INTEGER,
        path_classification TEXT NOT NULL,
        origin_story TEXT NOT NULL,
        academic_background TEXT NOT NULL,
        personal_effort_grind TEXT NOT NULL,
        current_workplace TEXT NOT NULL,
        first_recorded_earnings TEXT NOT NULL,
        current_financial_status TEXT NOT NULL,
        has_criminal_record BOOLEAN NOT NULL,
        legal_summary TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS milestones (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        candidate_id TEXT NOT NULL,
        milestone_type TEXT NOT NULL,
        description TEXT NOT NULL,
        FOREIGN KEY(candidate_id) REFERENCES profiles(candidate_id)
    );
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS citations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        candidate_id TEXT NOT NULL,
        title TEXT NOT NULL,
        url TEXT NOT NULL,
        category TEXT NOT NULL,
        FOREIGN KEY(candidate_id) REFERENCES profiles(candidate_id)
    );
    """)

    conn.commit()
    conn.close()

def save_dossier(dossier: CandidateDossier, db_path: Path = DB_PATH):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    cur.execute("""
    INSERT OR REPLACE INTO profiles VALUES (
        ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP
    );
    """, (
        dossier.candidate_id,
        dossier.category_tag,
        dossier.identity.full_name,
        ", ".join(dossier.identity.known_aliases),
        dossier.identity.nationality_or_location,
        dossier.identity.birth_year,
        dossier.identity.current_age,
        dossier.education.path_classification,
        dossier.education.origin_story_starting_age,
        dossier.education.academic_background,
        dossier.education.personal_effort_and_grind,
        dossier.career.current_workplace,
        dossier.financial.first_recorded_earnings,
        dossier.financial.current_estimated_earnings_or_funding,
        dossier.legal.has_criminal_record,
        dossier.legal.summary
    ))

    # Milestones & Certifications
    cur.execute("DELETE FROM milestones WHERE candidate_id = ?", (dossier.candidate_id,))
    for cert in dossier.education.certifications_and_milestones:
        cur.execute("INSERT INTO milestones (candidate_id, milestone_type, description) VALUES (?, ?, ?)",
                    (dossier.candidate_id, "Certification/Milestone", cert))
    for proj in dossier.career.notable_projects_or_cves:
        cur.execute("INSERT INTO milestones (candidate_id, milestone_type, description) VALUES (?, ?, ?)",
                    (dossier.candidate_id, "Project/CVE", proj))

    # Citations
    cur.execute("DELETE FROM citations WHERE candidate_id = ?", (dossier.candidate_id,))
    for cite in dossier.citations:
        cur.execute("INSERT INTO citations (candidate_id, title, url, category) VALUES (?, ?, ?, ?)",
                    (dossier.candidate_id, cite.title, cite.url, cite.category))

    conn.commit()
    conn.close()