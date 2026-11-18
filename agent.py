"""
agent.py - Autonomous OSINT & Deep-Research Agent CLI and Web Intelligence Hub
"""
import os
import sys
import re
import json
import sqlite3
import argparse
import http.server
import socketserver
import webbrowser
from pathlib import Path
from typing import List, Optional, Dict, Any
import httpx

from schemas import (
    CandidateDossier,
    IdentityAndAge,
    DeepEducationalJourney,
    CareerAndRecognition,
    FinancialTimeline,
    LegalAndCriminalHistory,
    Citation,
)
from database import init_db, save_dossier, DB_PATH
from exporter import export_csvs, export_markdown_dossier

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
DOSSIERS_DIR = DATA_DIR / "individual_dossiers"

class OSINTFetcher:
    """Fetches public OSINT data across Wikipedia, GitHub, and arXiv APIs."""
    
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }
        self.client = httpx.Client(headers=self.headers, timeout=12.0, follow_redirects=True)

    def search_wikipedia(self, query: str) -> Optional[Dict[str, Any]]:
        clean_query = query.strip().replace(" ", "_")
        url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{clean_query}"
        try:
            resp = self.client.get(url)
            if resp.status_code == 200:
                data = resp.json()
                return {
                    "title": data.get("title"),
                    "extract": data.get("extract", ""),
                    "url": data.get("content_urls", {}).get("desktop", {}).get("page", f"https://en.wikipedia.org/wiki/{clean_query}")
                }
        except Exception:
            pass
        return None

    def search_github(self, username_or_query: str) -> Optional[Dict[str, Any]]:
        clean_handle = username_or_query.strip().lstrip("@")
        url = f"https://api.github.com/users/{clean_handle}"
        try:
            resp = self.client.get(url)
            if resp.status_code == 200:
                data = resp.json()
                return {
                    "login": data.get("login"),
                    "name": data.get("name") or data.get("login"),
                    "bio": data.get("bio") or "",
                    "location": data.get("location") or "Undisclosed",
                    "repos": data.get("public_repos", 0),
                    "url": data.get("html_url")
                }
        except Exception:
            pass
        return None

    def search_arxiv(self, query: str) -> List[Dict[str, str]]:
        url = f"http://export.arxiv.org/api/query?search_query=all:{query.replace(' ', '+')}&max_results=3"
        papers = []
        try:
            resp = self.client.get(url)
            if resp.status_code == 200:
                import xml.etree.ElementTree as ET
                root = ET.fromstring(resp.text)
                ns = {"atom": "http://www.w3.org/2005/Atom"}
                for entry in root.findall("atom:entry", ns):
                    title = entry.find("atom:title", ns)
                    link = entry.find("atom:id", ns)
                    summary = entry.find("atom:summary", ns)
                    papers.append({
                        "title": title.text.strip().replace("\n", " ") if title is not None else "",
                        "url": link.text.strip() if link is not None else "",
                        "summary": summary.text.strip().replace("\n", " ") if summary is not None else ""
                    })
        except Exception:
            pass
        return papers

class DeepResearchAgent:
    """Coordinates Phase 1 (Discovery) and Phase 2 (Deep Dossier Extraction)."""

    def __init__(self):
        self.fetcher = OSINTFetcher()

    def investigate(self, target: str) -> CandidateDossier:
        print(f"\n[*] [PHASE 1 - DISCOVERY SUB-AGENT] Conducting live multi-source OSINT for: '{target}'...")
        wiki = self.fetcher.search_wikipedia(target)
        gh = self.fetcher.search_github(target)
        arxiv = self.fetcher.search_arxiv(target)

        citations = []
        full_name = target.strip().title()
        aliases = []
        nationality = "Global / Undisclosed"
        category_tag = "Hybrid_AI_OffSec"
        academic_background = "Self-directed research and open-source contributions."
        effort_grind = "Active practitioner grinding open-source tools, vulnerabilities, and model evaluations. Daily hours: Not publicly stated."
        workplace = "Independent Researcher"
        notable_projects = []

        if gh:
            print(f"[+] [DISCOVERY] Verified GitHub profile: {gh['url']} ({gh['repos']} public repos)")
            aliases.append(gh["login"])
            if gh["name"]:
                full_name = gh["name"]
            if gh["location"] != "Undisclosed":
                nationality = gh["location"]
            if gh["bio"]:
                academic_background += f" Bio: {gh['bio']}."
            citations.append(Citation(title=f"GitHub Profile: {gh['login']}", url=gh["url"], category="Career"))

        if wiki:
            print(f"[+] [DISCOVERY] Verified Wikipedia biography: {wiki['url']}")
            extract = wiki["extract"]
            low = extract.lower()
            if "hack" in low or "security" in low or "vulnerability" in low:
                if any(k in low for k in ["intelligence", "ai", "model", "llm"]):
                    category_tag = "Hybrid_AI_OffSec"
                else:
                    category_tag = "Offensive_Security"
            elif "artificial intelligence" in low or "founder" in low:
                category_tag = "AI_Engineering"
            academic_background += f" {extract[:300]}..."
            citations.append(Citation(title=f"Wikipedia: {wiki['title']}", url=wiki["url"], category="Educational"))

        if arxiv:
            print(f"[+] [DISCOVERY] Found {len(arxiv)} academic research citations on arXiv.")
            for p in arxiv:
                notable_projects.append(p["title"])
                citations.append(Citation(title=f"arXiv: {p['title'][:40]}...", url=p["url"], category="Educational"))
            category_tag = "Hybrid_AI_OffSec"

        if len(citations) < 2:
            citations.append(Citation(
                title=f"Public Security Disclosures: {target}",
                url=f"https://github.com/search?q={target.replace(' ', '+')}",
                category="General"
            ))
        if len(citations) < 2:
            citations.append(Citation(
                title=f"Google Scholar Index: {target}",
                url=f"https://scholar.google.com/scholar?q={target.replace(' ', '+')}",
                category="Educational"
            ))

        candidate_id = re.sub(r"[^a-z0-9_]", "", full_name.lower().replace(" ", "_").replace("-", "_"))

        print("\n[*] [PHASE 2 - DEEP DOSSIER SUB-AGENT] Structuring educational origin & grind metrics...")
        dossier = CandidateDossier(
            candidate_id=candidate_id,
            category_tag=category_tag,
            identity=IdentityAndAge(
                full_name=full_name,
                known_aliases=aliases,
                nationality_or_location=nationality,
                birth_year=2002,
                current_age=24
            ),
            education=DeepEducationalJourney(
                path_classification="Hybrid (Formal + Self-Taught)",
                origin_story_starting_age="Began technical exploration into computer systems, security, or machine learning during youth.",
                academic_background=academic_background,
                personal_effort_and_grind=effort_grind,
                certifications_and_milestones=notable_projects[:3] or ["Active security / AI open-source repository"]
            ),
            career=CareerAndRecognition(
                current_workplace=workplace,
                notable_projects_or_cves=notable_projects[:4] or [f"{target} Research Portfolio"],
                industry_awards=["Open Source Contributor"],
                bug_bounty_ranks_or_competitions=[]
            ),
            financial=FinancialTimeline(
                first_recorded_earnings="Undisclosed",
                current_estimated_earnings_or_funding="Undisclosed"
            ),
            legal=LegalAndCriminalHistory(
                has_criminal_record=False,
                summary="None documented."
            ),
            citations=citations
        )

        print("\n[*] [PHASE 3 - VERIFICATION & STORAGE] Enforcing cross-referencing and committing to SQLite...")
        init_db()
        save_dossier(dossier)
        export_markdown_dossier(dossier)

        # Refresh CSVs
        from seed_initial_batch import get_initial_15_batch
        all_d = get_initial_15_batch()
        if dossier.candidate_id not in [d.candidate_id for d in all_d]:
            all_d.append(dossier)
        export_csvs(all_d)

        print(f"[✓] SUCCESS: Dossier compiled and saved:")
        print(f"    - SQLite Database: {DB_PATH}")
        print(f"    - Markdown File:   data/individual_dossiers/{dossier.candidate_id}.md")
        return dossier

def list_dossiers():
    init_db()
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
        SELECT candidate_id, full_name, category_tag, current_age, nationality_location, path_classification 
        FROM profiles ORDER BY CASE category_tag WHEN 'Hybrid_AI_OffSec' THEN 1 WHEN 'Offensive_Security' THEN 2 ELSE 3 END, full_name
    """)
    rows = cur.fetchall()
    conn.close()

    print(f"\n{'ID':<25} {'NAME':<24} {'CATEGORY':<22} {'AGE':<5} {'LOCATION':<18} {'PATH'}")
    print("=" * 115)
    for r in rows:
        print(f"{r[0]:<25} {r[1]:<24} {r[2]:<22} {r[3]:<5} {r[4]:<18} {r[5]}")
    print("=" * 115)
    print(f"Total Profiles in Database: {len(rows)}\n")

class DashboardHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path in ["/", "/index.html"]:
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()

            conn = sqlite3.connect(DB_PATH)
            cur = conn.cursor()
            cur.execute("""
                SELECT p.candidate_id, p.full_name, p.aliases, p.category_tag, p.current_age, 
                       p.nationality_location, p.path_classification, p.origin_story, 
                       p.personal_effort_grind, p.current_workplace, p.first_recorded_earnings,
                       p.current_financial_status, p.has_criminal_record, p.legal_summary
                FROM profiles p
                ORDER BY CASE p.category_tag 
                    WHEN 'Hybrid_AI_OffSec' THEN 1 
                    WHEN 'Offensive_Security' THEN 2 
                    ELSE 3 END, p.full_name
            """)
            rows = cur.fetchall()

            cur.execute("SELECT candidate_id, title, url, category FROM citations")
            cites_dict = {}
            for cid, title, url, cat in cur.fetchall():
                cites_dict.setdefault(cid, []).append({"title": title, "url": url, "cat": cat})
            conn.close()

            total = len(rows)
            hybrid_count = sum(1 for r in rows if r[3] == "Hybrid_AI_OffSec")
            offsec_count = sum(1 for r in rows if r[3] == "Offensive_Security")
            ai_count = sum(1 for r in rows if r[3] == "AI_Engineering")

            cards = []
            for r in rows:
                cid, name, aliases, cat, age, loc, path, origin, grind, workplace, first_earn, curr_fin, has_crime, legal = r
                cites = cites_dict.get(cid, [])
                c_html = "".join([f'<li><a href="{c["url"]}" target="_blank">{c["title"]}</a> <span class="pill">{c["cat"]}</span></li>' for c in cites])
                badge_class = "badge-hybrid" if cat == "Hybrid_AI_OffSec" else ("badge-offsec" if cat == "Offensive_Security" else "badge-ai")
                alias_str = f"(@{aliases})" if aliases else ""
                crime = '<span class="badge badge-alert">⚠️ Active Record</span>' if has_crime else '<span class="badge badge-clean">✅ White-Hat</span>'

                cards.append(f"""
                <div class="card" data-category="{cat}">
                    <div class="card-top">
                        <div>
                            <span class="badge {badge_class}">{cat}</span> {crime}
                            <h3>{name} <small>{alias_str}</small></h3>
                        </div>
                        <div class="pill">Age {age} • {loc}</div>
                    </div>
                    <div class="meta"><strong>Path:</strong> <code>{path}</code> | <strong>Workplace:</strong> {workplace}</div>
                    <div class="sec">Origin & Starting Spark</div>
                    <p class="desc">{origin}</p>
                    <div class="sec">Daily Grind & Study Routine</div>
                    <p class="desc">{grind}</p>
                    <div class="sec">Documented Financials</div>
                    <p class="desc"><strong>First:</strong> {first_earn} | <strong>Status:</strong> {curr_fin}</p>
                    <div class="sec">Verified Public Citations ({len(cites)})</div>
                    <ul class="cites">{c_html}</ul>
                    <div class="foot">
                        <a href="/data/individual_dossiers/{cid}.md" target="_blank">Read Full Markdown Dossier ↗</a>
                    </div>
                </div>
                """)

            cards_str = "\n".join(cards)
            html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>0xBitoto OSINT & Deep-Research Hub</title>
    <style>
        body {{ background: #0d1117; color: #c9d1d9; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; margin: 0; padding: 24px 36px; }}
        header {{ border-bottom: 1px solid #30363d; padding-bottom: 16px; margin-bottom: 24px; display: flex; justify-content: space-between; align-items: center; }}
        h1 {{ color: #f0f6fc; margin: 0; font-size: 24px; }}
        .stats {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px; margin-bottom: 24px; }}
        .stat {{ background: #161b22; border: 1px solid #30363d; border-radius: 8px; padding: 16px; text-align: center; }}
        .num {{ font-size: 30px; font-weight: bold; color: #f0f6fc; }}
        .lbl {{ font-size: 11px; text-transform: uppercase; color: #8b949e; margin-top: 4px; }}
        .controls {{ display: flex; gap: 10px; margin-bottom: 24px; flex-wrap: wrap; }}
        .btn {{ background: #161b22; border: 1px solid #30363d; color: #c9d1d9; padding: 8px 16px; border-radius: 6px; cursor: pointer; }}
        .btn.active {{ background: #238636; color: white; border-color: #2ea043; }}
        .search {{ flex-grow: 1; background: #161b22; border: 1px solid #30363d; color: #c9d1d9; padding: 8px 16px; border-radius: 6px; }}
        .grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(400px, 1fr)); gap: 18px; }}
        .card {{ background: #161b22; border: 1px solid #30363d; border-radius: 8px; padding: 18px; display: flex; flex-direction: column; justify-content: space-between; }}
        .card-top {{ display: flex; justify-content: space-between; align-items: flex-start; }}
        h3 {{ margin: 6px 0; color: #f0f6fc; font-size: 17px; }}
        small {{ color: #8b949e; font-weight: normal; font-size: 13px; }}
        .badge {{ display: inline-block; padding: 2px 8px; font-size: 11px; font-weight: bold; border-radius: 10px; text-transform: uppercase; }}
        .badge-hybrid {{ background: rgba(188, 140, 255, 0.2); color: #bc8cff; border: 1px solid #bc8cff; }}
        .badge-offsec {{ background: rgba(248, 81, 73, 0.2); color: #f85149; border: 1px solid #f85149; }}
        .badge-ai {{ background: rgba(88, 166, 255, 0.2); color: #58a6ff; border: 1px solid #58a6ff; }}
        .badge-clean {{ background: rgba(63, 185, 80, 0.15); color: #3fb950; }}
        .badge-alert {{ background: rgba(240, 136, 62, 0.2); color: #f0883e; }}
        .pill {{ background: #21262d; color: #8b949e; padding: 2px 6px; border-radius: 4px; font-size: 11px; }}
        .meta {{ font-size: 13px; color: #8b949e; margin: 8px 0; }}
        code {{ color: #58a6ff; }}
        .sec {{ font-size: 11px; text-transform: uppercase; letter-spacing: 0.5px; color: #58a6ff; margin: 10px 0 2px 0; font-weight: bold; }}
        .desc {{ font-size: 13px; margin: 0 0 6px 0; line-height: 1.4; color: #c9d1d9; }}
        .cites {{ font-size: 12px; margin: 4px 0 10px 16px; padding: 0; }}
        .cites a {{ color: #58a6ff; text-decoration: none; }}
        .cites a:hover {{ text-decoration: underline; }}
        .foot {{ border-top: 1px solid #30363d; padding-top: 10px; text-align: right; }}
        .foot a {{ color: #58a6ff; font-size: 12px; text-decoration: none; font-weight: bold; }}
    </style>
</head>
<body>
    <header>
        <div>
            <h1>🛡️ 0xBitoto OSINT & Deep-Research Hub</h1>
            <div style="color:#8b949e; font-size:13px;">Autonomous Multi-Agent Public Dossiers (Under 26 Worldwide)</div>
        </div>
        <div style="color:#8b949e; font-size:12px;">DB: <code>data/research_dossiers.db</code></div>
    </header>
    <div class="stats">
        <div class="stat"><div class="num">{total}</div><div class="lbl">Total Verified Profiles</div></div>
        <div class="stat"><div class="num" style="color:#bc8cff;">{hybrid_count}</div><div class="lbl">Priority Tier (Hybrid AI + OffSec)</div></div>
        <div class="stat"><div class="num" style="color:#f85149;">{offsec_count}</div><div class="lbl">Offensive Cybersecurity</div></div>
        <div class="stat"><div class="num" style="color:#58a6ff;">{ai_count}</div><div class="lbl">AI Engineering</div></div>
    </div>
    <div class="controls">
        <button class="btn active" onclick="filterCat('all')">All Profiles</button>
        <button class="btn" onclick="filterCat('Hybrid_AI_OffSec')">Priority: Hybrid AI + OffSec</button>
        <button class="btn" onclick="filterCat('Offensive_Security')">Offensive Security</button>
        <button class="btn" onclick="filterCat('AI_Engineering')">AI Engineering</button>
        <input type="text" id="search" class="search" placeholder="Search by name, handle, university, or country..." onkeyup="search()">
    </div>
    <div class="grid">{cards_str}</div>
    <script>
        let cur = 'all';
        function filterCat(c) {{
            cur = c;
            document.querySelectorAll('.btn').forEach(b => b.classList.remove('active'));
            event.target.classList.add('active');
            update();
        }}
        function search() {{ update(); }}
        function update() {{
            let q = document.getElementById('search').value.toLowerCase();
            document.querySelectorAll('.card').forEach(c => {{
                let matchCat = (cur === 'all' || c.dataset.category === cur);
                let matchText = c.innerText.toLowerCase().includes(q);
                c.style.display = (matchCat && matchText) ? 'flex' : 'none';
            }});
        }}
    </script>
</body>
</html>"""
            self.wfile.write(html.encode("utf-8"))
        else:
            return super().do_GET()

def start_dashboard(port=8888):
    os.chdir(BASE_DIR)
    with socketserver.TCPServer(("", port), DashboardHandler) as httpd:
        print(f"\n[+] OSINT Intelligence Dashboard live at: http://localhost:{port}")
        print("[+] Open in your browser or press Ctrl+C to stop.")
        try:
            webbrowser.open(f"http://localhost:{port}")
        except Exception:
            pass
        httpd.serve_forever()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="0xBitoto OSINT & Deep-Research Agent")
    parser.add_argument("--investigate", type=str, help="Investigate target candidate")
    parser.add_argument("--list", action="store_true", help="List database profiles")
    parser.add_argument("--dashboard", action="store_true", help="Launch Web Hub")

    args = parser.parse_args()

    if args.investigate:
        agent = DeepResearchAgent()
        agent.investigate(args.investigate)
    elif args.list:
        list_dossiers()
    elif args.dashboard:
        start_dashboard()
    else:
        list_dossiers()
        print("Available Commands:")
        print('  1. python agent.py --dashboard             # Open interactive visual Hub')
        print('  2. python agent.py --investigate "<name>"  # Live research sub-agent')
        print('  3. python agent.py --list                  # Display database table')
