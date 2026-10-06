import re


# Initial technical skill dictionary.
# We will expand this substantially as the project develops.
TECHNICAL_SKILLS = {
    "python",
    "java",
    "c",
    "c++",
    "c#",
    "javascript",
    "typescript",
    "html",
    "css",
    "react",
    "react native",
    "next.js",
    "node.js",
    "express",
    "fastapi",
    "django",

    "data cleaning",
    "data visualization",
    "power query",
    "matplotlib",
    
    "sql",
    "mysql",
    "postgresql",
    "mongodb",

    "pandas",
    "numpy",
    "scikit-learn",
    "tensorflow",
    "pytorch",
    "keras",

    "machine learning",
    "deep learning",
    "natural language processing",
    "nlp",
    "computer vision",

    "power bi",
    "tableau",
    "excel",

    "aws",
    "azure",
    "google cloud",
    "docker",
    "kubernetes",

    "git",
    "github",
    "linux",

    "spark",
    "hadoop",
    "kafka",

    "supabase",
    "firebase",
}


def normalize_text(text: str) -> str:
    """Normalize resume text for easier matching."""

    text = text.lower()

    # Replace repeated whitespace with a single space
    text = re.sub(r"\s+", " ", text)

    return text.strip()


def extract_skills(text: str) -> list[str]:
    """
    Extract known technical skills from resume text.
    """

    normalized_text = normalize_text(text)

    found_skills = []

    for skill in TECHNICAL_SKILLS:

        # Escape special regex characters such as + and .
        pattern = r"(?<!\w)" + re.escape(skill) + r"(?!\w)"

        if re.search(pattern, normalized_text):
            found_skills.append(skill)

    return sorted(found_skills)