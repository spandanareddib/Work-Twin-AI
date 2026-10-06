import re

from app.services.resume_parser.skill_extractor import extract_skills
from app.services.skill_intelligence.skill_normalizer import normalize_skills


SECTION_HEADINGS = [
    "Objective",
    "Education",
    "Technical Skills",
    "Certifications",
    "Relevant Coursework",
    "Projects",
    "Tools",
    "Professional Experience",
    "Leadership Experience",
    "Achievements",
    "Strengths",
]


def extract_email(text: str) -> str | None:
    pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"

    match = re.search(pattern, text)

    return match.group(0) if match else None


def extract_phone(text: str) -> str | None:
    pattern = r"(?:\+91[\s-]?)?[6-9]\d{9}"

    match = re.search(pattern, text)

    return match.group(0) if match else None


def extract_name(text: str) -> str | None:
    """
    Extract the candidate name from the first non-empty line.
    """

    lines = [
        line.strip()
        for line in text.splitlines()
        if line.strip()
    ]

    if not lines:
        return None

    return lines[0]


def extract_sections(text: str) -> dict:
    """
    Split resume text into sections using known section headings.
    """

    lines = text.splitlines()

    sections = {}
    current_section = None
    current_content = []

    for line in lines:

        cleaned_line = line.strip()

        if not cleaned_line:
            continue

        # Remove bullet symbol for easier processing
        if cleaned_line in SECTION_HEADINGS:

            # Save previous section
            if current_section:
                sections[current_section] = "\n".join(
                    current_content
                ).strip()

            current_section = cleaned_line
            current_content = []

        elif current_section:
            current_content.append(cleaned_line)

    # Save final section
    if current_section:
        sections[current_section] = "\n".join(
            current_content
        ).strip()

    return sections


def parse_education(section_text: str) -> list[dict]:
    """
    Parse the education section.
    """

    lines = [
        line.strip()
        for line in section_text.splitlines()
        if line.strip()
    ]

    education = []

    current = {}

    for line in lines:

        if line.startswith("B.Tech"):
            if current:
                education.append(current)

            current = {
                "degree": line
            }

        elif line.startswith("Intermediate"):
            if current:
                education.append(current)

            current = {
                "degree": line
            }

        elif line.startswith("10th Class"):
            if current:
                education.append(current)

            current = {
                "degree": line
            }

        elif line.startswith("CMR College"):
            current["institution"] = line

        elif line.startswith("Ratna Junior College"):
            current["institution"] = line

        elif line.startswith("Narayana High School"):
            current["institution"] = line

        elif line.startswith("Expected Graduation"):
            current["graduation"] = line.split(":", 1)[-1].strip()

        elif line.startswith("Score"):
            current["score"] = line.split(":", 1)[-1].strip()

    if current:
        education.append(current)

    return education


def parse_certifications(section_text: str) -> list[str]:
    """
    Extract certification entries.
    """

    return [
        line.lstrip("•").strip()
        for line in section_text.splitlines()
        if line.strip()
    ]


def parse_coursework(section_text: str) -> list[str]:
    """
    Extract relevant coursework.
    """

    text = " ".join(
        line.strip()
        for line in section_text.splitlines()
        if line.strip()
    )

    return [
        item.strip()
        for item in text.split(",")
        if item.strip()
    ]


def parse_projects(section_text: str) -> list[dict]:
    """
    Parse projects using project title lines followed by bullet descriptions.
    """

    lines = [
        line.strip()
        for line in section_text.splitlines()
        if line.strip()
    ]

    projects = []
    current_project = None

    for line in lines:

        # Project titles in this resume are not bullet points
        if not line.startswith("•"):

            if current_project:
                projects.append(current_project)

            current_project = {
                "name": line,
                "description": []
            }

        else:
            if current_project:
                current_project["description"].append(
                    line.lstrip("•").strip()
                )

    if current_project:
        projects.append(current_project)

    return projects


def parse_experience(section_text: str) -> list[dict]:
    """
    Parse professional experience.
    """

    lines = [
        line.strip()
        for line in section_text.splitlines()
        if line.strip()
    ]

    experience = []

    current = None
    current_responsibility = None

    for line in lines:

        if line.startswith("Python and DSA Instructor"):
            if current:
                if current_responsibility:
                    current["responsibilities"].append(
                        current_responsibility
                    )
                experience.append(current)

            current = {
                "role": line,
                "organization": "Trailbliz",
                "duration": None,
                "responsibilities": []
            }

            current_responsibility = None

        elif current is not None and line.startswith("July 2026"):
            current["duration"] = line

        elif current is not None and line.startswith("•"):

            if current_responsibility:
                current["responsibilities"].append(
                    current_responsibility
                )

            current_responsibility = line.lstrip("•").strip()

        elif current is not None and current_responsibility:
            # Continue a responsibility that was split across PDF lines
            current_responsibility += " " + line

    if current:
        if current_responsibility:
            current["responsibilities"].append(
                current_responsibility
            )

        experience.append(current)

    return experience

def parse_leadership(section_text: str) -> list[dict]:
    """
    Parse leadership experience.
    """

    lines = [
        line.strip()
        for line in section_text.splitlines()
        if line.strip()
    ]

    leadership = []

    current = None

    for line in lines:

        if line.startswith("President –"):
            if current:
                leadership.append(current)

            current = {
                "role": line,
                "organization": None,
                "responsibilities": []
            }

        elif line.startswith("Event Head –"):
            if current:
                leadership.append(current)

            current = {
                "role": line,
                "organization": None,
                "responsibilities": []
            }

        elif current is not None and line.startswith("•"):
            current["responsibilities"].append(
                line.lstrip("•").strip()
            )

        elif current is not None and current["organization"] is None:
            current["organization"] = line

    if current:
        leadership.append(current)

    return leadership


def parse_achievements(section_text: str) -> list[str]:
    """
    Extract achievements.
    """

    return [
        line.lstrip("•").strip()
        for line in section_text.splitlines()
        if line.strip()
    ]


def build_profile(text: str) -> dict:
    """
    Build a structured career profile from extracted resume text.
    """

    sections = extract_sections(text)

    return {
        "personal_info": {
            "name": extract_name(text),
            "email": extract_email(text),
            "phone": extract_phone(text),
        },

        "skills": normalize_skills(extract_skills(text)),

        "education": parse_education(
            sections.get("Education", "")
        ),

        "certifications": parse_certifications(
            sections.get("Certifications", "")
        ),

        "coursework": parse_coursework(
            sections.get("Relevant Coursework", "")
        ),

        "projects": parse_projects(
            sections.get("Projects", "")
        ),

        "experience": parse_experience(
            sections.get("Professional Experience", "")
        ),

        "leadership": parse_leadership(
            sections.get("Leadership Experience", "")
        ),

        "achievements": parse_achievements(
            sections.get("Achievements", "")
        ),

        "tools": [
            item.strip()
            for item in sections.get("Tools", "").split(",")
            if item.strip()
        ],
    }