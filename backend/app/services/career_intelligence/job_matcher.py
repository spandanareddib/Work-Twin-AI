"""
Job Matching Engine for WorkTwin AI.

Calculates candidate-job compatibility using the
Skill Gap Analysis Engine.
"""

from app.services.job_intelligence.job_roles import get_all_job_roles
from app.services.career_intelligence.skill_gap import calculate_skill_gap


def rank_job_roles(candidate_skills: list[str]) -> list[dict]:
    """
    Calculate skill match scores for all available job roles
    and return them ranked from highest to lowest match.
    """

    results = []

    job_roles = get_all_job_roles()

    for job in job_roles:

        gap_analysis = calculate_skill_gap(
            candidate_skills=candidate_skills,
            required_skills=job["required_skills"]
        )

        results.append({
            "role": job["role"],
            "category": job["category"],
            "match_percentage": gap_analysis["match_percentage"],
            "matched_skills": gap_analysis["matched_skills"],
            "missing_skills": gap_analysis["missing_skills"],
        })

    results.sort(
        key=lambda item: item["match_percentage"],
        reverse=True
    )

    return results


def get_top_job_matches(
    candidate_skills: list[str],
    top_n: int = 5
) -> list[dict]:
    """
    Return the top N job-role matches.
    """

    ranked_roles = rank_job_roles(candidate_skills)

    return ranked_roles[:top_n]