# 🛡️ 0xBitoto: Autonomous Multi-Agent OSINT & Deep-Research Pipeline

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Pydantic v2](https://img.shields.io/badge/Validation-Pydantic%20v2-e92063.svg?logo=pydantic&logoColor=white)](https://docs.pydantic.dev/)
[![SQLite](https://img.shields.io/badge/Database-SQLite3-003B57.svg?logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Production%20Ready-brightgreen.svg)](#)

> **Autonomous multi-agent OSINT and biographical research pipeline designed to discover, verify, cross-reference, and compile exhaustive intelligence dossiers on notable prodigies and innovators under 26 years old worldwide.**

---

## 📑 Table of Contents
- [Executive Overview](#-executive-overview)
- [Domain Tiers](#-domain-tiers)
- [System Architecture & Agent Lifecycle](#-system-architecture--agent-lifecycle)
- [Anti-Hallucination & Verification Protocol](#-anti-hallucination--verification-protocol)
- [Repository Structure](#-repository-structure)
- [Quickstart & Usage](#-quickstart--usage)
  - [1. Launch Interactive Web Intelligence Hub](#1-launch-interactive-web-intelligence-hub)
  - [2. Live Sub-Agent OSINT Investigation](#2-live-sub-agent-osint-investigation)
  - [3. CLI Database Inspection](#3-cli-database-inspection)
  - [4. Batch Pipeline Execution](#4-batch-pipeline-execution)
- [Seed Dataset (16 High-Signal Dossiers)](#-seed-dataset-16-high-signal-dossiers)
- [Relational Database Schema](#-relational-database-schema)
- [Ethics & Responsible OSINT](#-ethics--responsible-osint)
- [Pushing to Your GitHub](#-pushing-to-your-github)

---

## 🔭 Executive Overview

Traditional biographical data collection often suffers from LLM hallucinations, outdated milestones, ungrounded metrics, and lack of cross-referencing. **0xBitoto** solves this by implementing a **deterministic, parallel multi-agent pipeline**:

1. **Autonomous Discovery Sub-Agents**: Fan out in parallel across public registers, academic preprint archives (arXiv), developer graphs (GitHub), HackerOne/Bugcrowd rankings, and official public court press releases (DOJ/UK CPS).
2. **Deep Extraction Sub-Agents**: Dissect interviews, podcast transcripts, AMA threads, and biographical articles to extract verifiable origins, study routines, and milestones into a strict, validated schema.
3. **Verification & Storage Engine**: Enforces strict negative constraints, validates at least two independent source URLs, commits structured relational entities to SQLite (`research_dossiers.db`), and exports filterable CSVs and clean Markdown dossiers.

---

## 🎯 Domain Tiers

The pipeline monitors and categorizes candidates across three primary domains:

| Category Tier | Description & Scope | Target Archetypes |
| :--- | :--- | :--- |
| **`Hybrid_AI_OffSec`** <br>*(Priority Tier)* | Individuals actively operating at the convergence of Offensive Cybersecurity and AI Engineering. | AI Red-Teamers, LLM Jailbreak Researchers, Adversarial ML Practitioners, Automated Vulnerability Discovery Tool Authors. |
| **`Offensive_Security`** | World-class ethical hackers, exploit developers, and documented court-convicted cybercriminals. | Bug bounty record holders ($1M+ payouts), DEF CON CTF champions, zero-day researchers, and public DOJ/CPS indicted threat actors. |
| **`AI_Engineering`** | Visionary AI researchers, open-source maintainers, and venture-backed founders. | Foundational model contributors, prompt architecture pioneers, autonomous agent creators, and AI governance leaders. |

---

## ⚙️ System Architecture & Agent Lifecycle

```
[ PHASE 1: DISCOVERY SUB-AGENTS (Parallel) ]
  ├── Sources: arXiv, GitHub API, Wikipedia API, HackerOne, DEF CON Rosters, DOJ/Court Records
  └── Filter: Under 26 Years Old (as of 2026) or primary defining milestones achieved under 26
        │
        ▼
[ PHASE 2: DEEP DOSSIER & ORIGIN EXTRACTION (Fan-Out) ]
  ├── Identity & Age: Full name, aliases, nationality, verified birth year
  ├── Deep Educational Journey:
  │     ├── Path: Strictly Self-Taught | Formal University | University Dropout | Hybrid
  │     ├── Origin Spark: Exact starting age and catalyst event
  │     ├── Academic Background: Institutions, degrees, GPA/honors, dropout rationale
  │     └── Daily Grind Routine: Study habits, hours/day, CTF schedules, home labs
  ├── Career & Recognition: Current lab/workplace, CVEs, awards, rankings
  ├── Financial Timeline: First documented earnings, funding rounds, net worth
  └── Legal / Criminal Record: Formal court convictions, attack vectors, restitution
        │
        ▼
[ PHASE 3: VERIFICATION, COMPLIANCE & STORAGE ]
  ├── Strict Anti-Hallucination Gate (No guessed metrics)
  ├── Dual-Source Cross-Referencing (>= 2 verified public URLs)
  ├── SQLite Relational Database (research_dossiers.db)
  ├── Filtered CSV Exports (hybrid_ai_offsec, offensive_sec, ai_eng)
  └── Individual Narrative Markdown Dossiers (individual_dossiers/*.md)
```

---

## 🛡️ Anti-Hallucination & Verification Protocol

To maintain high data integrity, `schemas.py` enforces strict Pydantic v2 validation rules:
- **Daily Grind Hours Rule**: If daily/weekly study hours are not explicitly stated in verified interviews or articles, the field defaults strictly to `"Not publicly stated"`. Guessing or extrapolating hours is prohibited.
- **Financial Rule**: Personal net worth or compensation without official public disclosures (e.g., funding press releases, Forbes valuations, or bounty payout announcements) defaults strictly to `"Undisclosed"`.
- **Dual-Citation Guarantee**: Every profile requires at least two independent, verified source URLs across educational, financial, or career claims before committing to SQLite.
- **Legal Record Authenticity**: Criminal records are exclusively recorded if backed by formal government/court records (e.g., DOJ, FBI, Crown Prosecution Service).

---

## 📂 Repository Structure

```
0xBitoto/
├── data/
│   ├── research_dossiers.db            # Relational SQLite database
│   ├── hybrid_ai_offsec_under26.csv    # Priority Tier filterable export
│   ├── offensive_security_under26.csv  # Offensive Cybersecurity export
│   ├── ai_engineering_under26.csv      # AI Engineering export
│   └── individual_dossiers/            # Full narrative Markdown dossiers
│       ├── alex_albert.md
│       ├── alexandr_wang.md
│       ├── arion_kurtaj.md
│       ├── bishal_biswas.md
│       ├── conor_brian_fitzpatrick.md
│       ├── cosmin_iordache.md
│       ├── david_schutz.md
│       ├── div_garg.md
│       ├── edoardo_debenedetti.md
│       ├── george_hotz.md
│       ├── jack_cable.md
│       ├── javier_rando.md
│       ├── matt_shumer.md
│       ├── santiago_lopez.md
│       ├── sayash_kapoor.md
│       └── sneha_revanur.md
├── agent.py                            # Multi-agent CLI & Web Intelligence Hub
├── database.py                         # SQLite schema, tables & ORM logic
├── exporter.py                         # CSV export and Markdown generator
├── run_pipeline.py                     # Parallel multi-agent pipeline runner
├── schemas.py                          # Strict Pydantic v2 data models
├── seed_initial_batch.py               # Initial verified batch loader
├── requirements.txt                    # Project dependencies
└── README.md                           # Documentation
```

---

## 🚀 Quickstart & Usage

### Prerequisites
- Python 3.10+
- `pip`

```bash
git clone https://github.com/<your-username>/0xBitoto.git
cd 0xBitoto
pip install -r requirements.txt
```

---

### 1. Launch Interactive Web Intelligence Hub

Start the zero-dependency, dark-themed OSINT Intelligence Dashboard:

```bash
python agent.py --dashboard
```

Navigate to `http://localhost:8888` in your browser:
- **Live Metrics**: Total verified dossiers, Priority Tier counts, OffSec, and AI breakdown.
- **Filter Controls**: One-click filtering by domain category.
- **Instant Search**: Filter cards in real time by name, alias, university, or country.
- **Deep Origin Cards**: Expandable dossier cards with origin stories, daily grind schedules, financial timelines, and direct clickable source links.

---

### 2. Live Sub-Agent OSINT Investigation

Trigger the autonomous sub-agent pipeline to investigate any target individual in real time:

```bash
python agent.py --investigate "<name_or_handle>"
```

*Example:*
```bash
python agent.py --investigate "geohot"
```

**Terminal Telemetry:**
```text
[*] [PHASE 1 - DISCOVERY SUB-AGENT] Conducting live multi-source OSINT for: 'geohot'...
[+] [DISCOVERY] Verified GitHub profile: https://github.com/geohot (103 public repos)
[+] [DISCOVERY] Verified Wikipedia biography: https://en.wikipedia.org/wiki/George_Hotz
[*] [PHASE 2 - DEEP DOSSIER SUB-AGENT] Structuring educational origin & grind metrics...
[*] [PHASE 3 - VERIFICATION & STORAGE] Enforcing cross-referencing and committing to SQLite...
[✓] SUCCESS: Dossier compiled and saved:
    - SQLite Database: data/research_dossiers.db
    - Markdown File:   data/individual_dossiers/george_hotz.md
```

---

### 3. CLI Database Inspection

Output a formatted tabular report of all stored candidates directly in your terminal:

```bash
python agent.py --list
```

---

### 4. Batch Pipeline Execution

Re-run the parallel worker pool to regenerate and verify all initial candidate dossiers:

```bash
python run_pipeline.py
```

---

## 📊 Seed Dataset (16 High-Signal Dossiers)

| Candidate Name | Category Tag | Age | Nationality | Educational Path | Primary Claim to Fame / Defining Milestone |
| :--- | :--- | :---: | :--- | :--- | :--- |
| **Jack Cable** | `Hybrid_AI_OffSec` | 26 | USA | Formal University | Top 3 in DoD Hack the Pentagon at 16; CISA Senior Advisor leading AI Red-Teaming. |
| **Alex Albert** | `Hybrid_AI_OffSec` | 25 | USA | Formal University | Founded JailbreakChat.com; cataloged 1,000+ adversarial LLM jailbreaks; Anthropic DevRel Lead. |
| **Javier Rando** | `Hybrid_AI_OffSec` | 25 | Spain / CH | Formal University | ETH Zurich SRI Lab; co-author of universal adversarial triggers on aligned LLMs; DEF CON AI Village. |
| **Edoardo Debenedetti** | `Hybrid_AI_OffSec` | 25 | Italy / CH | Formal University | ETH Zurich / ELLIS; pioneer in training data extraction attacks against production LLMs (ChatGPT). |
| **Sayash Kapoor** | `Hybrid_AI_OffSec` | 26 | India / USA | Formal University | Princeton CITP; co-author of *AI Snake Oil*; AI safety auditor cited in U.S. Senate AI hearings. |
| **George Hotz** | `Hybrid_AI_OffSec` | 24* | USA | Hybrid | World's first iPhone hardware unlock at 17; PS3 jailbreak; TinyGrad neural framework creator. |
| **Santiago Lopez** | `Offensive_Security` | 26 | Argentina | Self-Taught | World's first bug bounty millionaire at age 19 on HackerOne; reported 1,600+ vulnerabilities. |
| **Cosmin Iordache** | `Offensive_Security` | 26 | Romania / DE | Hybrid | Second hacker to hit $2M on HackerOne (at age 20); multiple-time HackerOne MVP belt winner. |
| **David Schütz** | `Offensive_Security` | 25 | Hungary | Self-Taught | Discovered CVE-2022-20465 (Android Lockscreen Bypass via SIM PUK reset); awarded $70k bounty by Google. |
| **Bishal Biswas** | `Offensive_Security` | 23 | India | Self-Taught | Inducted into Hall of Fame of 50+ Fortune 500s and US DoD; top-ranked Bugcrowd ethical hacker. |
| **Arion Kurtaj** | `Offensive_Security` | 21 | UK | Self-Taught | Lapsus$ hacking leader; breached Rockstar Games/GTA 6, Uber, Nvidia; sentenced to hospital order. |
| **Conor Brian Fitzpatrick**| `Offensive_Security` | 24 | USA | Self-Taught | Admin of BreachForums (330k members); exploited FBI LEEP portal; arrested and sentenced by DOJ. |
| **Div Garg** | `AI_Engineering` | 25 | India / USA | Dropout | Stanford AI Lab; published RL models at NeurIPS; founder of MultiOn autonomous browser agent. |
| **Sneha Revanur** | `AI_Engineering` | 22 | USA | Formal University | Youngest on TIME 100 AI (at 18); founder of Encode Justice; youth advisor to the White House on AI. |
| **Matt Shumer** | `AI_Engineering` | 26 | USA | Dropout | Founded OthersideAI / HyperWrite at age 20; creator of open-source Reflection 70B LLM. |
| **Alexandr Wang** | `AI_Engineering` | 29* | USA | Dropout | MIT dropout at 19; founded Scale AI; became world's youngest self-made billionaire at age 24. |

*\* Milestone achieved under 26.*

---

## 🗄️ Relational Database Schema

The pipeline automatically creates and manages `research_dossiers.db`:

```sql
CREATE TABLE profiles (
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

CREATE TABLE milestones (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    candidate_id TEXT NOT NULL,
    milestone_type TEXT NOT NULL,
    description TEXT NOT NULL,
    FOREIGN KEY(candidate_id) REFERENCES profiles(candidate_id)
);

CREATE TABLE citations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    candidate_id TEXT NOT NULL,
    title TEXT NOT NULL,
    url TEXT NOT NULL,
    category TEXT NOT NULL,
    FOREIGN KEY(candidate_id) REFERENCES profiles(candidate_id)
);
```

---

## ⚖️ Ethics & Responsible OSINT

- **Exclusively Public Telemetry**: All data collected is sourced exclusively from open public records, scholarly preprint servers (arXiv), conference rosters (DEF CON, Black Hat), public code repositories (GitHub), and official government publications (DOJ, FTC, UK CPS).
- **No Private PII**: This project strictly avoids harvesting private personal identifiable information (such as personal residential addresses, private phone numbers, or private correspondence).
- **Educational & Defensive Purpose**: Built to study technical learning journeys, self-directed study habits, and the intersection of AI safety and offensive cybersecurity.

---
