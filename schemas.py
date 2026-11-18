"""
schemas.py - Data Validation & Pydantic Models for OSINT Deep-Research Pipeline
"""
from typing import List, Optional, Literal
from pydantic import BaseModel, Field, HttpUrl, field_validator

PathClassification = Literal[
    "Strictly Self-Taught",
    "Formal University",
    "University Dropout",
    "Hybrid (Formal + Self-Taught)"
]

CategoryTag = Literal[
    "Hybrid_AI_OffSec",       # Priority Tier
    "Offensive_Security",
    "AI_Engineering"
]

class Citation(BaseModel):
    title: str = Field(..., description="Source name or article title")
    url: str = Field(..., description="Direct public URL")
    category: Literal["Educational", "Career", "Financial", "Legal", "General"]

class IdentityAndAge(BaseModel):
    full_name: str
    known_aliases: List[str] = Field(default_factory=list)
    nationality_or_location: str
    birth_year: Optional[int] = None
    current_age: int = Field(..., description="Current age as of 2026 or age at milestone")
    age_confirmed: bool = True

class DeepEducationalJourney(BaseModel):
    path_classification: PathClassification
    origin_story_starting_age: str = Field(..., description="Exact age and catalyst event")
    academic_background: str = Field(..., description="Schools, universities, degrees, GPAs/honors, or dropout rationale")
    personal_effort_and_grind: str = Field(
        ..., 
        description="Documented study habits, hours/week (or 'Not publicly stated'), home lab setups, CTF grinds, mentors"
    )
    certifications_and_milestones: List[str] = Field(
        default_factory=list, 
        description="Formal certs (OSCP, etc.) or self-taught milestones (first CVE, first repo)"
    )

class CareerAndRecognition(BaseModel):
    current_workplace: str
    notable_projects_or_cves: List[str] = Field(default_factory=list)
    industry_awards: List[str] = Field(default_factory=list)
    bug_bounty_ranks_or_competitions: List[str] = Field(default_factory=list)

class FinancialTimeline(BaseModel):
    first_recorded_earnings: str = Field(
        ..., 
        description="First payout/prize/salary, age at time, or 'Undisclosed'"
    )
    current_estimated_earnings_or_funding: str = Field(
        ..., 
        description="Documented funding rounds, net worth, or 'Undisclosed'"
    )

class LegalAndCriminalHistory(BaseModel):
    has_criminal_record: bool
    summary: str = Field(
        default="None documented.", 
        description="Arrests, indictments, attack methods, financial gains, legal outcomes, or 'None'"
    )

class CandidateDossier(BaseModel):
    candidate_id: str
    category_tag: CategoryTag
    identity: IdentityAndAge
    education: DeepEducationalJourney
    career: CareerAndRecognition
    financial: FinancialTimeline
    legal: LegalAndCriminalHistory
    citations: List[Citation] = Field(..., min_length=2)

    @field_validator("citations")
    def verify_minimum_citations(cls, v):
        if len(v) < 2:
            raise ValueError("Cross-referencing requires at least two verified public citations.")
        return v