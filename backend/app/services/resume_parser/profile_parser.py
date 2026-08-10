import re

from app.services.resume_parser.skill_extractor import extract_skills


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
    Basic name extraction.

    This is intentionally a baseline implementation.
    We will improve it later using NLP/NER.
    """

    lines = [
        line.strip()
        for line in text.splitlines()
        if line.strip()
    ]

    if not lines:
        return None

    return lines[0]


def build_profile(text: str) -> dict:
    return {
        "personal_info": {
            "name": extract_name(text),
            "email": extract_email(text),
            "phone": extract_phone(text),
        },
        "skills": extract_skills(text),
        "education": [],
        "experience": [],
        "projects": [],
        "certifications": [],
    }