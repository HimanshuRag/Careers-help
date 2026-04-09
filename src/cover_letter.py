"""Cover letter planning module.

This module generates bullet points for crafting a personalized cover letter
based on the evaluation of a job description.
"""
from typing import Dict, Any

from .evaluation import EvaluationResult

def plan_cover_letter(eval_result: EvaluationResult) -> Dict[str, Any]:
    """
    Given an EvaluationResult, produce a dictionary containing talking points
    to include in a cover letter.

    :param eval_result: Result of evaluating a job description.
    :return: A dictionary with the role title, company, and a list of cover letter points.
    """
    points = []
    dims = eval_result.dimensions

    # Always mention your enthusiasm for the role and company
    points.append(
        f"Express enthusiasm for the {eval_result.title} role at {eval_result.company}."
    )

    # Highlight technical experience if skills alignment is moderate or low
    if dims.get("skills_alignment", 0) < 3:
        points.append(
            "Highlight your AI, machine learning, data, and Python experience that matches the job requirements."
        )

    # Emphasize success with remote work if the role is remote-friendly
    if dims.get("remote", 0) == 5:
        points.append(
            "Emphasize your success working remotely and your ability to collaborate effectively across locations."
        )

    # Convey adaptability and growth mindset for seniority stretch
    if dims.get("seniority_stretch", 0) < 3:
        points.append(
            "Convey your adaptability and eagerness to take on new responsibilities and grow into a more senior role."
        )

    # Share impact stories if impact dimension is low
    if dims.get("impact", 0) < 3:
        points.append(
            "Share an example of a project where your contributions created measurable impact."
        )

    return {
        "title": eval_result.title,
        "company": eval_result.company,
        "points": points,
    }
