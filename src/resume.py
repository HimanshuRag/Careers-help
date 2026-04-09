"""Resume planning module.

This module provides functionality to generate suggestions for updating a resume
based on the results of a job description evaluation.
"""
from typing import Dict, Any

from .evaluation import EvaluationResult

def plan_resume_updates(eval_result: EvaluationResult) -> Dict[str, Any]:
    """
    Given an EvaluationResult, return a dictionary with resume suggestions.

    The suggestions aim to help tailor your resume towards the evaluated job
    by highlighting areas that need improvement or emphasis. If the evaluation
    indicates strong alignment across all dimensions, a generic positive note
    is returned instead.

    :param eval_result: Result of evaluating a job description.
    :return: A dictionary containing the job title, company, and a list of suggestions.
    """
    suggestions = []
    dims = eval_result.dimensions

    # Suggest focusing on technical skills if skills alignment is low
    if dims.get("skills_alignment", 0) < 3:
        suggestions.append(
            "Emphasize your relevant AI, machine learning, data, and Python experience in the summary and bullet points."
        )

    # Suggest mentioning remote readiness
    if dims.get("remote", 0) == 0:
        suggestions.append(
            "Clarify your willingness or ability to work remotely, or mention any prior remote work experience."
        )

    # Suggest highlighting leadership or growth potential
    if dims.get("seniority_stretch", 0) < 3:
        suggestions.append(
            "Frame your accomplishments to showcase leadership, mentoring, or senior-level impact where applicable."
        )

    if dims.get("growth", 0) < 3:
        suggestions.append(
            "Include examples that demonstrate adaptability, learning new technologies, and driving growth."
        )

    # If there are no targeted suggestions, provide a positive note
    if not suggestions:
        suggestions.append(
            "Your resume appears well-aligned with this role. Highlight quantifiable achievements and results."
        )

    return {
        "title": eval_result.title,
        "company": eval_result.company,
        "suggestions": suggestions,
    }
