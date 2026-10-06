"""
Skill Gap Analysis Engine for WorkTwin AI.

Compares a candidate's normalized skills against
the required skills for a target job role.
"""


def calculate_skill_gap(
    candidate_skills: list[str],
    required_skills: list[str]
) -> dict:
    """
    Calculate the skill match between a candidate
    and a target job role.
    """

    candidate_set = {
        skill.strip().lower()
        for skill in candidate_skills
    }

    required_set = {
        skill.strip().lower()
        for skill in required_skills
    }

    matched_skills = sorted(
        candidate_set.intersection(required_set)
    )

    missing_skills = sorted(
        required_set - candidate_set
    )

    total_required = len(required_set)

    if total_required == 0:
        match_percentage = 0.0
    else:
        match_percentage = round(
            (len(matched_skills) / total_required) * 100,
            2
        )

    return {
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "match_percentage": match_percentage,
        "matched_count": len(matched_skills),
        "required_count": total_required,
    }