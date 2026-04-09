from dataclasses import dataclass
from typing import Dict

@dataclass
class EvaluationResult:
    title: str
    company: str
    description: str
    dimensions: Dict[str, int]
    score: float
    grade: str

def evaluate_job_description(title: str, company: str, description: str) -> EvaluationResult:
    """
    Evaluate a job description across several dimensions and return an EvaluationResult.
    This is a simplified heuristic implementation. Adjust the scoring logic to fit
    your actual evaluation criteria and desired weighting.
    """
    # Initialize dimensions with zero scores.
    dimensions = {
        "role_match": 0,
        "skills_alignment": 0,
        "seniority_stretch": 0,
        "compensation": 0,
        "remote": 0,
        "sector": 0,
        "culture": 0,
        "growth": 0,
        "stability": 0,
        "impact": 0,
    }

    # Define keywords for a very naive skills match heuristic.
    keywords = ["AI", "Machine Learning", "Python", "Data"]

    # Count occurrences of each keyword as part of the skills alignment score.
    description_lower = description.lower()
    for kw in keywords:
        if kw.lower() in description_lower:
            dimensions["skills_alignment"] += 1

    # Set the remote score if the job explicitly mentions remote work.
    if "remote" in description_lower:
        dimensions["remote"] = 5

    # Compute a simple overall score: sum of dimension scores divided by max possible.
    max_dimension_score = 5 * len(dimensions)
    total_score = sum(dimensions.values())
    score_percentage = (total_score / max_dimension_score) * 100 if max_dimension_score else 0

    # Convert numeric score to a grade.
    if score_percentage >= 80:
        grade = "A"
    elif score_percentage >= 60:
        grade = "B"
    elif score_percentage >= 40:
        grade = "C"
    elif score_percentage >= 20:
        grade = "D"
    else:
        grade = "F"

    return EvaluationResult(
        title=title,
        company=company,
        description=description,
        dimensions=dimensions,
        score=score_percentage,
        grade=grade,
    )
