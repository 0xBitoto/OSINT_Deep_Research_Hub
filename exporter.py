"""
exporter.py - Export SQLite Dossiers into Filtered CSVs and Markdown Dossiers
"""
import csv
from pathlib import Path
from typing import List
from schemas import CandidateDossier

DATA_DIR = Path(__file__).resolve().parent / "data"
DOSSIER_DIR = DATA_DIR / "individual_dossiers"

def export_csvs(dossiers: List[CandidateDossier]):
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    
    csv_configs = {
        "Hybrid_AI_OffSec": DATA_DIR / "hybrid_ai_offsec_under26.csv",
        "Offensive_Security": DATA_DIR / "offensive_security_under26.csv",
        "AI_Engineering": DATA_DIR / "ai_engineering_under26.csv"
    }

    fieldnames = [
        "Candidate ID", "Full Name", "Aliases", "Current Age", "Nationality",
        "Education Path", "Starting Spark", "Daily Grind & Habits", 
        "Current Lab / Company", "First Earnings", "Financial Status", 
        "Legal Record", "Primary Citations"
    ]

    for category, filepath in csv_configs.items():
        filtered = [d for d in dossiers if d.category_tag == category]
        with open(filepath, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(fieldnames)
            for d in filtered:
                writer.writerow([
                    d.candidate_id,
                    d.identity.full_name,
                    ", ".join(d.identity.known_aliases),
                    d.identity.current_age,
                    d.identity.nationality_or_location,
                    d.education.path_classification,
                    d.education.origin_story_starting_age,
                    d.education.personal_effort_and_grind,
                    d.career.current_workplace,
                    d.financial.first_recorded_earnings,
                    d.financial.current_estimated_earnings_or_funding,
                    d.legal.summary if d.legal.has_criminal_record else "Clean",
                    " | ".join([f"{c.title}: {c.url}" for c in d.citations])
                ])

def export_markdown_dossier(dossier: CandidateDossier):
    DOSSIER_DIR.mkdir(parents=True, exist_ok=True)
    slug = dossier.candidate_id
    md_path = DOSSIER_DIR / f"{slug}.md"

    md_content = f"""# OSINT Intelligence Dossier: {dossier.identity.full_name}

**Category Tag:** `{dossier.category_tag}`  
**Known Aliases/Handles:** {', '.join(dossier.identity.known_aliases) if dossier.identity.known_aliases else 'None'}  
**Nationality / Base:** {dossier.identity.nationality_or_location}  
**Age / Birth Year:** {dossier.identity.current_age} (Born: {dossier.identity.birth_year or 'Undisclosed'})  
**Current Workplace/Affiliation:** {dossier.career.current_workplace}

---

## 1. Educational Journey & Daily Grind (Deep Origin)
* **Educational Path Classification:** `{dossier.education.path_classification}`
* **Origin Spark & Starting Age:** {dossier.education.origin_story_starting_age}
* **Academic Background:** {dossier.education.academic_background}
* **Personal Effort, Grind & Daily Routine:**  
  {dossier.education.personal_effort_and_grind}

### Technical Milestones & Certifications
{chr(10).join([f'- {m}' for m in dossier.education.certifications_and_milestones])}

---

## 2. Career, Projects & Recognition
* **Notable Projects & CVEs:**  
{chr(10).join([f'  - {p}' for p in dossier.career.notable_projects_or_cves])}
* **Awards & Honours:**  
{chr(10).join([f'  - {a}' for a in dossier.career.industry_awards])}
* **Competitive Ranks:**  
{chr(10).join([f'  - {r}' for r in dossier.career.bug_bounty_ranks_or_competitions])}

---

## 3. Documented Financial Timeline
* **First Recorded Earnings:** {dossier.financial.first_recorded_earnings}
* **Current Publicly Documented Status / Funding:** {dossier.financial.current_estimated_earnings_or_funding}

---

## 4. Legal / Criminal History
* **Status:** {'⚠️ Active Record' if dossier.legal.has_criminal_record else '✅ Clean / White-Hat Only'}
* **Legal Details:**  
  {dossier.legal.summary}

---

## 5. Primary Verified Citations
{chr(10).join([f'- [{c.title}]({c.url}) ({c.category})' for c in dossier.citations])}
"""
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(md_content)