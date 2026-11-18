"""
run_pipeline.py - Orchestration of Discovery Sub-Agents & Deep Extraction
"""
import concurrent.futures
from typing import List
from schemas import CandidateDossier
from database import init_db, save_dossier
from exporter import export_csvs, export_markdown_dossier
from seed_initial_batch import get_initial_15_batch

def execute_pipeline(batch: List[CandidateDossier]):
    print("=== [PHASE 1] Autonomous Discovery & Tagging Initialized ===")
    print(f"Total Candidates in Queue: {len(batch)}")
    
    print("\n=== [PHASE 2] Deep Educational Extraction & Cross-Referencing Fan-Out ===")
    init_db()

    def process_candidate(candidate: CandidateDossier):
        print(f"[*] Processing {candidate.identity.full_name} ({candidate.category_tag})...")
        save_dossier(candidate)
        export_markdown_dossier(candidate)
        return candidate.candidate_id

    # Parallel sub-agent execution
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        results = list(executor.map(process_candidate, batch))
    
    print(f"\n[+] Successfully compiled {len(results)} individual dossiers into SQLite & Markdown.")

    print("\n=== [PHASE 3] Generating Filtered CSV Exports ===")
    export_csvs(batch)
    print("[+] Exported:")
    print("    - data/hybrid_ai_offsec_under26.csv")
    print("    - data/offensive_security_under26.csv")
    print("    - data/ai_engineering_under26.csv")

if __name__ == "__main__":
    initial_batch = get_initial_15_batch()
    execute_pipeline(initial_batch)