SKILL_ALIASES = {
    "python": "Python",
    "java": "Java",
    "c": "C",
    "c++": "C++",
    "c#": "C#",
    "javascript": "JavaScript",
    "typescript": "TypeScript",

    "html": "HTML",
    "html5": "HTML",
    "css": "CSS",
    "css3": "CSS",
    "react": "React",
    "react.js": "React",
    "react native": "React Native",
    "next.js": "Next.js",
    "node.js": "Node.js",
    "express": "Express.js",

    "sql": "SQL",
    "mysql": "MySQL",
    "postgresql": "PostgreSQL",
    "mongodb": "MongoDB",

    "numpy": "NumPy",
    "pandas": "Pandas",
    "matplotlib": "Matplotlib",
    "scikit-learn": "Scikit-learn",

    "machine learning": "Machine Learning",
    "machine learning fundamentals": "Machine Learning",
    "deep learning": "Deep Learning",
    "deep learning fundamentals": "Deep Learning",
    "natural language processing": "Natural Language Processing",
    "nlp": "Natural Language Processing",
    "computer vision": "Computer Vision",

    "excel": "Microsoft Excel",
    "microsoft excel": "Microsoft Excel",
    "power bi": "Power BI",
    "power query": "Power Query",
    "data cleaning": "Data Cleaning",
    "data visualization": "Data Visualization",

    "git": "Git",
    "github": "GitHub",
    "linux": "Linux",
    "docker": "Docker",
    "kubernetes": "Kubernetes",

    "aws": "AWS",
    "azure": "Microsoft Azure",
    "google cloud": "Google Cloud",

    "fastapi": "FastAPI",
    "django": "Django",
    "supabase": "Supabase",
    "firebase": "Firebase",
}


def normalize_skill(skill: str) -> str:
    normalized = skill.strip().lower()

    return SKILL_ALIASES.get(
        normalized,
        skill.strip()
    )


def normalize_skills(skills: list[str]) -> list[str]:
    normalized_skills = {
        normalize_skill(skill)
        for skill in skills
    }

    return sorted(normalized_skills)
