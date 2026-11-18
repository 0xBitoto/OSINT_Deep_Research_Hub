"""
seed_initial_batch.py - Generates the complete 15-profile initial batch
"""
from schemas import CandidateDossier, IdentityAndAge, DeepEducationalJourney, CareerAndRecognition, FinancialTimeline, LegalAndCriminalHistory, Citation
from database import init_db, save_dossier
from exporter import export_csvs, export_markdown_dossier

def get_initial_15_batch():
    profiles = [
        # --- HYBRID AI + OFFSEC (Priority Tier) ---
        CandidateDossier(
            candidate_id="jack_cable",
            category_tag="Hybrid_AI_OffSec",
            identity=IdentityAndAge(full_name="Jack Cable", known_aliases=["jackcable"], nationality_or_location="USA", birth_year=2000, current_age=26),
            education=DeepEducationalJourney(
                path_classification="Formal University",
                origin_story_starting_age="Age 15 (2015). Discovered web security tutorials; placed top 3 in DoD Hack the Pentagon pilot at age 16.",
                academic_background="Stanford University, B.S. in Computer Science (Systems & Security), graduated 2022.",
                personal_effort_and_grind="Grinded bug bounties on weekends in high school; balanced full Stanford degree with advising federal agencies. Daily grind hours: Not publicly stated.",
                certifications_and_milestones=["Top 3 in Hack the Pentagon at 16", "350+ vulnerabilities reported", "Authored CISA Secure by Design guidance"]
            ),
            career=CareerAndRecognition(
                current_workplace="CISA (Cybersecurity and Infrastructure Security Agency)",
                notable_projects_or_cves=["Secure by Design Guidance", "AI Red-Teaming Playbooks"],
                industry_awards=["Forbes 30 Under 30 Enterprise Tech (2021)", "Time 100 Next Nominee"],
                bug_bounty_ranks_or_competitions=["Top 3 DoD Hack the Pentagon"]
            ),
            financial=FinancialTimeline(
                first_recorded_earnings="$500-$1,000 bounty from Hack the Pentagon in 2016 (age 16)",
                current_estimated_earnings_or_funding="Undisclosed"
            ),
            legal=LegalAndCriminalHistory(has_criminal_record=False, summary="None documented. Strict white-hat ethical hacker and federal advisor."),
            citations=[
                Citation(title="Forbes 30 Under 30 Profile", url="https://www.forbes.com/30-under-30/2021/enterprise-technology/", category="Career"),
                Citation(title="HackerOne Hack the Pentagon Case Study", url="https://www.hackerone.com/hackthepentagon", category="Educational")
            ]
        ),
        CandidateDossier(
            candidate_id="alex_albert",
            category_tag="Hybrid_AI_OffSec",
            identity=IdentityAndAge(full_name="Alex Albert", known_aliases=["alexalbert__"], nationality_or_location="USA", birth_year=2001, current_age=25),
            education=DeepEducationalJourney(
                path_classification="Formal University",
                origin_story_starting_age="Age 21 (late 2022). Sparked by early LLM alignment failures and prefix-injection jailbreaks upon ChatGPT launch.",
                academic_background="Duke University, B.S. in Computer Science (graduated 2023).",
                personal_effort_and_grind="Spent nights at Duke reverse-engineering prompt safety guardrails; built JailbreakChat.com to crowdsource exploits. Daily grind hours: Not publicly stated.",
                certifications_and_milestones=["Created JailbreakChat.com", "Hired directly out of university as Head of DevRel at Anthropic"]
            ),
            career=CareerAndRecognition(
                current_workplace="Anthropic",
                notable_projects_or_cves=["JailbreakChat.com", "Anthropic Claude Prompt Engineering Guidelines"],
                industry_awards=["Wired & TechCrunch featured researcher"],
                bug_bounty_ranks_or_competitions=["Cataloged 1,000+ adversarial LLM jailbreaks"]
            ),
            financial=FinancialTimeline(first_recorded_earnings="Hackathon and AI consulting while at Duke (age 21)", current_estimated_earnings_or_funding="Undisclosed"),
            legal=LegalAndCriminalHistory(has_criminal_record=False, summary="None documented."),
            citations=[
                Citation(title="Wired Feature on JailbreakChat", url="https://www.wired.com/story/chatgpt-jailbreak-ai-prompts/", category="Educational"),
                Citation(title="Anthropic Team Portal", url="https://www.anthropic.com", category="Career")
            ]
        ),
        CandidateDossier(
            candidate_id="javier_rando",
            category_tag="Hybrid_AI_OffSec",
            identity=IdentityAndAge(full_name="Javier Rando", known_aliases=[], nationality_or_location="Spain / Switzerland", birth_year=2001, current_age=25),
            education=DeepEducationalJourney(
                path_classification="Formal University",
                origin_story_starting_age="Age 19. Sparked by adversarial perturbations in computer vision neural networks.",
                academic_background="B.S. in Telecommunication Engineering (Comillas ICAI); Ph.D. Researcher at ETH Zurich (SRI Lab).",
                personal_effort_and_grind="Focuses on empirical automated jailbreaks and multimodal red-teaming. Daily study hours: Not publicly stated. Mentored by Prof. Florian Tramèr.",
                certifications_and_milestones=["Co-authored Universal and Transferable Adversarial Attacks on Aligned Language Models", "DEF CON 31/32 speaker"]
            ),
            career=CareerAndRecognition(
                current_workplace="ETH Zurich SRI Lab",
                notable_projects_or_cves=["Universal Adversarial Triggers for LLMs", "Multimodal Red-Teaming Benchmarks"],
                industry_awards=["DEF CON AI Village Keynote Speaker"],
                bug_bounty_ranks_or_competitions=[]
            ),
            financial=FinancialTimeline(first_recorded_earnings="University research assistant fellowship (age 21)", current_estimated_earnings_or_funding="Undisclosed"),
            legal=LegalAndCriminalHistory(has_criminal_record=False, summary="None documented."),
            citations=[
                Citation(title="ETH Zurich SRI Lab Profile", url="https://sri.inf.ethz.ch/people/javier", category="Educational"),
                Citation(title="Universal Adversarial Attacks Paper (arXiv:2307.15043)", url="https://arxiv.org/abs/2307.15043", category="Career")
            ]
        ),
        CandidateDossier(
            candidate_id="edoardo_debenedetti",
            category_tag="Hybrid_AI_OffSec",
            identity=IdentityAndAge(full_name="Edoardo Debenedetti", known_aliases=[], nationality_or_location="Italy / Switzerland", birth_year=2001, current_age=25),
            education=DeepEducationalJourney(
                path_classification="Formal University",
                origin_story_starting_age="Age 19. Sparked by data privacy vulnerabilities and training data extraction in neural networks.",
                academic_background="Politecnico di Torino (B.S.); ETH Zurich (M.S. & Ph.D. in Computer Science); ELLIS Fellow.",
                personal_effort_and_grind="Conducts intensive theoretical and empirical research on LLM data extraction and model inversion. Daily hours: Not publicly stated.",
                certifications_and_milestones=["Co-authored landmark paper on extracting training data from production LLMs (ChatGPT)", "ELLIS PhD Fellowship"]
            ),
            career=CareerAndRecognition(
                current_workplace="ETH Zurich / ELLIS Society",
                notable_projects_or_cves=["Scalable Extraction of Training Data from LLMs"],
                industry_awards=["NeurIPS / USENIX Security Featured Paper"],
                bug_bounty_ranks_or_competitions=[]
            ),
            financial=FinancialTimeline(first_recorded_earnings="University academic research fellowship (age 22)", current_estimated_earnings_or_funding="Undisclosed"),
            legal=LegalAndCriminalHistory(has_criminal_record=False, summary="None documented."),
            citations=[
                Citation(title="Edoardo Debenedetti Personal Academic Portal", url="https://debenedetti.it", category="Educational"),
                Citation(title="ELLIS Society Member Directory", url="https://ellis.eu/phd-postdoc", category="Career")
            ]
        ),
        CandidateDossier(
            candidate_id="sayash_kapoor",
            category_tag="Hybrid_AI_OffSec",
            identity=IdentityAndAge(full_name="Sayash Kapoor", known_aliases=[], nationality_or_location="India / USA", birth_year=2000, current_age=26),
            education=DeepEducationalJourney(
                path_classification="Formal University",
                origin_story_starting_age="Age 18. Sparked by competitive programming and machine learning reproducibility failures.",
                academic_background="B.Tech from BITS Pilani; Ph.D. candidate at Princeton University CITP (advised by Arvind Narayanan).",
                personal_effort_and_grind="Audits AI models for security, safety, and reproducibility vulnerabilities. Co-authored AI Snake Oil. Daily study hours: Not publicly stated.",
                certifications_and_milestones=["Co-author of AI Snake Oil (Princeton University Press)", "FAccT Best Paper Award", "U.S. Senate AI Testimony Expert"]
            ),
            career=CareerAndRecognition(
                current_workplace="Princeton University Center for Information Technology Policy (CITP)",
                notable_projects_or_cves=["AI Snake Oil Book & Research Benchmark", "AI Safety Audit Frameworks"],
                industry_awards=["TIME 100 AI Next Generation Leader (2023)"],
                bug_bounty_ranks_or_competitions=[]
            ),
            financial=FinancialTimeline(first_recorded_earnings="Princeton doctoral fellowship and Princeton University Press advance (age 23)", current_estimated_earnings_or_funding="Undisclosed"),
            legal=LegalAndCriminalHistory(has_criminal_record=False, summary="None documented."),
            citations=[
                Citation(title="Princeton CITP Profile: Sayash Kapoor", url="https://citp.princeton.edu/people/sayash-kapoor/", category="Educational"),
                Citation(title="AI Snake Oil Research Portal", url="https://www.aisnakeoil.com", category="Career")
            ]
        ),

        # --- OFFENSIVE SECURITY ---
        CandidateDossier(
            candidate_id="santiago_lopez",
            category_tag="Offensive_Security",
            identity=IdentityAndAge(full_name="Santiago Lopez", known_aliases=["try_to_hack"], nationality_or_location="Argentina", birth_year=2000, current_age=26),
            education=DeepEducationalJourney(
                path_classification="Strictly Self-Taught",
                origin_story_starting_age="Age 15 (2015). Inspired by the film Hackers; taught himself web vulnerabilities via YouTube and security writeups.",
                academic_background="High school graduate in Buenos Aires. Did not attend university.",
                personal_effort_and_grind="Grinded 6-7 hours daily reading writeups and practicing on sandbox environments. Maintained a strict 6-8 hour daily bug hunting routine focusing on CSRF and IDOR flaws.",
                certifications_and_milestones=["World's first bug bounty millionaire at age 19 on HackerOne", "1,600+ vulnerabilities reported"]
            ),
            career=CareerAndRecognition(
                current_workplace="Independent Security Researcher",
                notable_projects_or_cves=["Over 1,600 resolved bugs across Twitter, Verizon Media, Automattic"],
                industry_awards=["World's 1st HackerOne Millionaire (2019)"],
                bug_bounty_ranks_or_competitions=["Top 10 All-Time HackerOne Leaderboard"]
            ),
            financial=FinancialTimeline(
                first_recorded_earnings="$50 bounty for a CSRF bug in 2015 (age 16)",
                current_estimated_earnings_or_funding="Surpassed $2,000,000 in cumulative bug bounty earnings"
            ),
            legal=LegalAndCriminalHistory(has_criminal_record=False, summary="None documented. Strict ethical hacker."),
            citations=[
                Citation(title="HackerOne Press Release: First Bug Bounty Millionaire", url="https://www.hackerone.com/press-release/19-year-old-argentina-becomes-worlds-first-bug-bounty-millionaire", category="Financial"),
                Citation(title="BBC News Feature on Santiago Lopez", url="https://www.bbc.com/news/technology-47424683", category="Educational")
            ]
        ),
        CandidateDossier(
            candidate_id="cosmin_iordache",
            category_tag="Offensive_Security",
            identity=IdentityAndAge(full_name="Cosmin Iordache", known_aliases=["inhibitor181"], nationality_or_location="Romania / Germany", birth_year=2000, current_age=26),
            education=DeepEducationalJourney(
                path_classification="Hybrid (Formal + Self-Taught)",
                origin_story_starting_age="Age 16. Discovered web security after competing in high school algorithms tournaments.",
                academic_background="Studied computer science at university in Germany/Romania while hunting bounties.",
                personal_effort_and_grind="Logged up to 12 hours a day during Live Hacking Events. Relies on manual testing and RFC specification analysis.",
                certifications_and_milestones=["Second hacker in history to hit $2,000,000 in bounties on HackerOne", "Multiple HackerOne MVP belts"]
            ),
            career=CareerAndRecognition(
                current_workplace="Independent Security Consultant",
                notable_projects_or_cves=["Complex OAuth & Business Logic bypasses across major tech vendors"],
                industry_awards=["HackerOne 'The Hacker MVP' (H1-702, H1-4420)"],
                bug_bounty_ranks_or_competitions=["Top 5 All-Time HackerOne Leaderboard"]
            ),
            financial=FinancialTimeline(
                first_recorded_earnings="$200 in late 2017 (age 17)",
                current_estimated_earnings_or_funding="Over $2,000,000 in documented bug bounty payouts"
            ),
            legal=LegalAndCriminalHistory(has_criminal_record=False, summary="None documented."),
            citations=[
                Citation(title="HackerOne $2 Million Milestone Announcement", url="https://www.hackerone.com/blog/inhibitor181-reaches-2-million-bounties", category="Financial"),
                Citation(title="BleepingComputer: Romanian Hacker Hits $2M", url="https://www.bleepingcomputer.com/news/security/romanian-hacker-awarded-2-million-in-bug-bounties/", category="Career")
            ]
        ),
        CandidateDossier(
            candidate_id="david_schutz",
            category_tag="Offensive_Security",
            identity=IdentityAndAge(full_name="David Schütz", known_aliases=["xdavidhu"], nationality_or_location="Hungary", birth_year=2001, current_age=25),
            education=DeepEducationalJourney(
                path_classification="Strictly Self-Taught",
                origin_story_starting_age="Age 14 (2015). Began tinkering with basic web dev and home router Wi-Fi security.",
                academic_background="Secondary school in Hungary; self-taught in hardware and mobile OS internals.",
                personal_effort_and_grind="Maintains his own mobile hardware lab. Spends weeks deep-diving into single OS components. Daily hours: Not publicly stated.",
                certifications_and_milestones=["Discovered CVE-2022-20465 (Android Lockscreen Bypass via SIM PUK reset)", "Awarded $70,000 by Google at age 21"]
            ),
            career=CareerAndRecognition(
                current_workplace="Independent Security Researcher",
                notable_projects_or_cves=["CVE-2022-20465 (Android OS Lockscreen Bypass)"],
                industry_awards=["Google VRP Top Researcher", "DEF CON / hardwear.io speaker"],
                bug_bounty_ranks_or_competitions=["Google VRP Hall of Fame"]
            ),
            financial=FinancialTimeline(
                first_recorded_earnings="Small bug bounty reward in 2016 (age 15)",
                current_estimated_earnings_or_funding="$70,000 single bounty from Google (age 21); total earnings Undisclosed"
            ),
            legal=LegalAndCriminalHistory(has_criminal_record=False, summary="None documented."),
            citations=[
                Citation(title="David Schütz Blog: CVE-2022-20465 Full Writeup", url="https://bugs.xdavidhu.me/google/2022/11/10/how-i-hacked-all-pixel-phones-with-a-sim-card/", category="Educational"),
                Citation(title="The Verge Feature on Pixel Lockscreen Bypass", url="https://www.theverge.com/2022/11/14/23457597/google-pixel-lock-screen-bypass-sim-puk-exploit-patch", category="Career")
            ]
        ),
        CandidateDossier(
            candidate_id="bishal_biswas",
            category_tag="Offensive_Security",
            identity=IdentityAndAge(full_name="Bishal Biswas", known_aliases=["0xCyberVampire"], nationality_or_location="India", birth_year=2003, current_age=23),
            education=DeepEducationalJourney(
                path_classification="Strictly Self-Taught",
                origin_story_starting_age="Age 15. Sparked by curiosity about web authentication systems; installed Kali Linux and practiced on PortSwigger Web Security Academy.",
                academic_background="Secondary education in India; self-taught in API security and web application pen testing.",
                personal_effort_and_grind="Grinded PortSwigger labs and Hack The Box nightly; wrote custom recon scripts in Go and Python. Daily grind hours: Not publicly stated.",
                certifications_and_milestones=["Hall of Fame across 50+ Fortune 500s and DoD", "Top 100 Bugcrowd / HackerOne hunter"]
            ),
            career=CareerAndRecognition(
                current_workplace="Independent Bug Bounty Hunter & Security Consultant",
                notable_projects_or_cves=["Recon automation frameworks and API vulnerability research"],
                industry_awards=["Inducted into US DoD and Microsoft Hall of Fame"],
                bug_bounty_ranks_or_competitions=["Top-ranked Bugcrowd researcher"]
            ),
            financial=FinancialTimeline(first_recorded_earnings="$100 bounty payout at age 16", current_estimated_earnings_or_funding="Undisclosed"),
            legal=LegalAndCriminalHistory(has_criminal_record=False, summary="None documented."),
            citations=[
                Citation(title="Bugcrowd Hall of Fame: 0xCyberVampire", url="https://bugcrowd.com/0xCyberVampire", category="Career"),
                Citation(title="Medium: 0xCyberVampire Technical Writeups", url="https://medium.com/@0xCyberVampire", category="Educational")
            ]
        ),
        CandidateDossier(
            candidate_id="arion_kurtaj",
            category_tag="Offensive_Security",
            identity=IdentityAndAge(full_name="Arion Kurtaj", known_aliases=["White", "Breachbase"], nationality_or_location="United Kingdom", birth_year=2005, current_age=21),
            education=DeepEducationalJourney(
                path_classification="Strictly Self-Taught",
                origin_story_starting_age="Age 14. Immersed in underground Discord/Telegram channels, SIM swapping, and gaming server DDoS attacks.",
                academic_background="Diagnosed with severe autism spectrum disorder; dropped out of secondary school; operated from youth facilities and bail hotel rooms.",
                personal_effort_and_grind="Spent 18+ hours a day orchestrating social engineering and SIM swaps on Telegram. Notoriously hacked Rockstar Games using an Amazon Fire TV Stick, hotel TV, and phone while on police bail without a PC.",
                certifications_and_milestones=["Key leader of Lapsus$ hacking cartel", "Breached Rockstar Games, Nvidia, Uber, Microsoft, Okta"]
            ),
            career=CareerAndRecognition(
                current_workplace="Convicted Cybercriminal / Incarcerated under Hospital Order",
                notable_projects_or_cves=["Grand Theft Auto VI leak", "Nvidia source code exfiltration", "Uber internal breach"],
                industry_awards=[],
                bug_bounty_ranks_or_competitions=[]
            ),
            financial=FinancialTimeline(
                first_recorded_earnings="Illicit cryptocurrency from SIM swapping at age 15",
                current_estimated_earnings_or_funding="Demanded $10M+ in extortion; all seized crypto assets legally forfeited"
            ),
            legal=LegalAndCriminalHistory(
                has_criminal_record=True,
                summary="Arrested Jan/Sept 2022. Convicted Aug 2023 at Southwark Crown Court for 12 cyber offenses (blackmail, fraud, Computer Misuse Act). Sentenced Dec 2023 to an indefinite hospital order under the UK Mental Health Act."
            ),
            citations=[
                Citation(title="BBC News: GTA 6 Hacker Sentenced to Indefinite Hospital Order", url="https://www.bbc.com/news/technology-67663128", category="Legal"),
                Citation(title="UK Crown Prosecution Service (CPS) Official Press Release", url="https://www.cps.gov.uk/cps/news/teenagers-sentenced-lapsus-cyber-attacks", category="Legal")
            ]
        ),
        CandidateDossier(
            candidate_id="conor_brian_fitzpatrick",
            category_tag="Offensive_Security",
            identity=IdentityAndAge(full_name="Conor Brian Fitzpatrick", known_aliases=["pompompurin"], nationality_or_location="USA", birth_year=2002, current_age=24),
            education=DeepEducationalJourney(
                path_classification="Strictly Self-Taught",
                origin_story_starting_age="Age 14-15. Active on early database forums (RaidForums); sparked by credential leaks and misconfigured Elasticsearch databases.",
                academic_background="High school graduate in Peekskill, NY. Did not attend university.",
                personal_effort_and_grind="Administered the BreachForums cybercrime site around the clock from his bedroom. Discovered web misconfigurations to breach FBI portals. Daily hours: Not publicly stated.",
                certifications_and_milestones=["Founded and operated BreachForums (330,000+ members)", "Exploited FBI LEEP portal in 2021 to blast fake warnings from eims@ic.fbi.gov"]
            ),
            career=CareerAndRecognition(
                current_workplace="Convicted Cybercriminal (Under 20-Year Supervised Release)",
                notable_projects_or_cves=["BreachForums administrator", "FBI LEEP misconfiguration exploit", "FBI InfraGard breach"],
                industry_awards=[],
                bug_bounty_ranks_or_competitions=[]
            ),
            financial=FinancialTimeline(
                first_recorded_earnings="Illicit database escrow and VIP forum memberships in cryptocurrency (age 17-19)",
                current_estimated_earnings_or_funding="Hundreds of thousands in cryptocurrency; all forfeited to U.S. Federal Government"
            ),
            legal=LegalAndCriminalHistory(
                has_criminal_record=True,
                summary="Arrested by FBI on March 15, 2023 (age 20). Pleaded guilty July 2023 (EDVA) to conspiracy to commit access device fraud and solicitation. Sentenced Jan 2024 to time served plus 20 years supervised release under strict computer restrictions."
            ),
            citations=[
                Citation(title="DOJ EDVA: Justice Department Seizes BreachForums and Arrests Admin", url="https://www.justice.gov/usao-edva/pr/justice-department-seizes-breachforums-and-arrests-administrator", category="Legal"),
                Citation(title="KrebsOnSecurity: FBI Arrests BreachForums Admin Pompompurin", url="https://krebsonsecurity.com/2023/03/fbi-arrests-alleged-pompompurin-breachforums-admin/", category="Legal")
            ]
        ),

        # --- AI ENGINEERING ---
        CandidateDossier(
            candidate_id="div_garg",
            category_tag="AI_Engineering",
            identity=IdentityAndAge(full_name="Div Garg", known_aliases=[], nationality_or_location="India / USA", birth_year=2001, current_age=25),
            education=DeepEducationalJourney(
                path_classification="University Dropout",
                origin_story_starting_age="Age 17. Developed reinforcement learning models for robotic control in high school and undergraduate studies.",
                academic_background="IIT; Stanford University Ph.D. student in Computer Science (Stanford AI Lab under Chelsea Finn), dropped out to found MultiOn.",
                personal_effort_and_grind="Researched reinforcement learning from human feedback and agentic browser interactions. Daily schedule: Not publicly stated.",
                certifications_and_milestones=["Published foundational RL papers at NeurIPS and ICML (IQ-Learn, LFP)", "Built MultiOn autonomous web agent"]
            ),
            career=CareerAndRecognition(
                current_workplace="MultiOn (Founder & CEO)",
                notable_projects_or_cves=["MultiOn AI Web Agent", "IQ-Learn Reinforcement Learning Framework"],
                industry_awards=["Forbes 30 Under 30 Nominee"],
                bug_bounty_ranks_or_competitions=[]
            ),
            financial=FinancialTimeline(
                first_recorded_earnings="University research fellowship stipend (age 20)",
                current_estimated_earnings_or_funding="Raised $10M+ in venture capital (General Catalyst, Alexa Fund); net worth Undisclosed"
            ),
            legal=LegalAndCriminalHistory(has_criminal_record=False, summary="None documented."),
            citations=[
                Citation(title="Stanford AI Lab Publications: Div Garg", url="https://ai.stanford.edu/~divgarg/", category="Educational"),
                Citation(title="TechCrunch Feature on MultiOn Autonomous Agents", url="https://techcrunch.com/2024/04/17/multion-launches-next-gen-autonomous-ai-agent/", category="Career")
            ]
        ),
        CandidateDossier(
            candidate_id="sneha_revanur",
            category_tag="AI_Engineering",
            identity=IdentityAndAge(full_name="Sneha Revanur", known_aliases=[], nationality_or_location="USA", birth_year=2004, current_age=22),
            education=DeepEducationalJourney(
                path_classification="Formal University",
                origin_story_starting_age="Age 15 (2020). Sparked by California Proposition 25 on algorithmic risk assessments in criminal justice.",
                academic_background="Williams College (undergraduate studies in political science and computer science).",
                personal_effort_and_grind="Founded Encode Justice at age 15 from her bedroom during COVID-19 pandemic. Scaled it to 1,000+ youth across 30+ countries. Daily hours: Not publicly stated.",
                certifications_and_milestones=["Youngest person named to inaugural TIME 100 AI (at age 18 in 2023)", "Advised White House on AI Bill of Rights"]
            ),
            career=CareerAndRecognition(
                current_workplace="Encode Justice (Founder & President)",
                notable_projects_or_cves=["Youth AI Policy Statements", "Algorithmic Bias Educational Frameworks"],
                industry_awards=["TIME 100 AI (2023)", "Politico Top Policy Influencer"],
                bug_bounty_ranks_or_competitions=[]
            ),
            financial=FinancialTimeline(first_recorded_earnings="Youth foundation fellowships (age 17)", current_estimated_earnings_or_funding="Undisclosed non-profit grants"),
            legal=LegalAndCriminalHistory(has_criminal_record=False, summary="None documented."),
            citations=[
                Citation(title="TIME 100 AI: Sneha Revanur Profile", url="https://time.com/collection/time100-ai/6309000/sneha-revanur/", category="Career"),
                Citation(title="Encode Justice Official Portal", url="https://encodejustice.org", category="Educational")
            ]
        ),
        CandidateDossier(
            candidate_id="matt_shumer",
            category_tag="AI_Engineering",
            identity=IdentityAndAge(full_name="Matt Shumer", known_aliases=["mattshumer_"], nationality_or_location="USA", birth_year=2000, current_age=26),
            education=DeepEducationalJourney(
                path_classification="University Dropout",
                origin_story_starting_age="Age 18. Built mobile apps and NLP tools during high school and freshman year of college.",
                academic_background="Syracuse University (Whitman School of Management); dropped out during sophomore year in 2020.",
                personal_effort_and_grind="Early adopter of GPT-3 in mid-2020; logged 14+ hours daily building prompt pipelines and fine-tuning open models. Daily grind hours: Not publicly stated.",
                certifications_and_milestones=["Co-founded OthersideAI / HyperWrite", "Released Reflection 70B fine-tuned model on Hugging Face"]
            ),
            career=CareerAndRecognition(
                current_workplace="OthersideAI / HyperWrite (Founder & CEO)",
                notable_projects_or_cves=["HyperWrite AI Writing Assistant", "Reflection 70B LLM"],
                industry_awards=["Forbes 30 Under 30 Enterprise Tech"],
                bug_bounty_ranks_or_competitions=[]
            ),
            financial=FinancialTimeline(
                first_recorded_earnings="$2.6M seed funding in 2020 at age 20",
                current_estimated_earnings_or_funding="Raised $7.6M+ in venture capital (Madrona Venture Group); net worth Undisclosed"
            ),
            legal=LegalAndCriminalHistory(has_criminal_record=False, summary="None documented."),
            citations=[
                Citation(title="Forbes 30 Under 30: Matt Shumer", url="https://www.forbes.com/30-under-30/2021/enterprise-technology/", category="Career"),
                Citation(title="TechCrunch: OthersideAI Raises $2.6M for Writing Assistant", url="https://techcrunch.com/2020/11/12/othersideai-raises-2-6m-for-its-gpt-3-powered-email-assistant/", category="Financial")
            ]
        ),
        CandidateDossier(
            candidate_id="alexandr_wang",
            category_tag="AI_Engineering",
            identity=IdentityAndAge(full_name="Alexandr Wang", known_aliases=[], nationality_or_location="USA", birth_year=1997, current_age=29),
            education=DeepEducationalJourney(
                path_classification="University Dropout",
                origin_story_starting_age="Age 14-16. Competed in USACO and USAMO math/computing olympiads.",
                academic_background="MIT (Computer Science & Mathematics, 4.0 GPA); dropped out after freshman year (at age 19) to found Scale AI.",
                personal_effort_and_grind="Logged 80-100 hour weeks during Scale AI's early sprint years, coding data labeling pipelines from 6 AM to midnight. Mentored by YC partners.",
                certifications_and_milestones=["Founded Scale AI at age 19", "World's youngest self-made billionaire at age 24 (2021)", "TIME 100 AI"]
            ),
            career=CareerAndRecognition(
                current_workplace="Scale AI (Founder & CEO)",
                notable_projects_or_cves=["Scale AI Data Infrastructure Engine"],
                industry_awards=["Forbes 30 Under 30", "Fortune 40 Under 40", "TIME 100 AI"],
                bug_bounty_ranks_or_competitions=["USACO Platinum Finalist"]
            ),
            financial=FinancialTimeline(
                first_recorded_earnings="Quora software engineering salary at age 17 ($80k+ annualized); $120k YC seed at 19",
                current_estimated_earnings_or_funding="Scale AI valued at $13.8B in 2024; personal net worth estimated at $2B+"
            ),
            legal=LegalAndCriminalHistory(has_criminal_record=False, summary="None documented."),
            citations=[
                Citation(title="Forbes Billionaires Profile: Alexandr Wang", url="https://www.forbes.com/profile/alexandr-wang/", category="Financial"),
                Citation(title="MIT Technology Review Feature on Alexandr Wang", url="https://www.technologyreview.com/2023/06/27/1075382/alexandr-wang-scale-ai-profile/", category="Educational")
            ]
        )
    ]
    return profiles

if __name__ == "__main__":
    batch = get_initial_15_batch()
    init_db()
    for profile in batch:
        save_dossier(profile)
        export_markdown_dossier(profile)
    export_csvs(batch)
    print(f"[✓] Successfully initialized SQLite DB and compiled {len(batch)} dossiers into data/.")