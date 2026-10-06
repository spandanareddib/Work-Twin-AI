"""
Job Role Knowledge Base for WorkTwin AI.

This module defines the initial career roles and their
core technical skill requirements.

This is a curated baseline dataset for the prototype.
It will later be expanded using real job-market data.
"""


JOB_ROLES = [
    {
        "role": "Data Analyst",
        "category": "Data",
        "description": "Analyzes data to generate business insights and support decision making.",
        "required_skills": [
            "Python",
            "SQL",
            "Microsoft Excel",
            "Power BI",
            "Data Cleaning",
            "Data Visualization",
            "Statistics",
        ],
    },

    {
        "role": "Data Scientist",
        "category": "Data Science",
        "description": "Uses statistics, machine learning, and programming to build data-driven solutions.",
        "required_skills": [
            "Python",
            "SQL",
            "Pandas",
            "NumPy",
            "Machine Learning",
            "Deep Learning",
            "Statistics",
            "Data Visualization",
        ],
    },

    {
        "role": "Machine Learning Engineer",
        "category": "Artificial Intelligence",
        "description": "Develops, trains, evaluates, and deploys machine learning systems.",
        "required_skills": [
            "Python",
            "SQL",
            "NumPy",
            "Pandas",
            "Scikit-learn",
            "Machine Learning",
            "Deep Learning",
            "Git",
            "Docker",
        ],
    },

    {
        "role": "AI Engineer",
        "category": "Artificial Intelligence",
        "description": "Builds AI-powered applications using machine learning and modern AI technologies.",
        "required_skills": [
            "Python",
            "Machine Learning",
            "Deep Learning",
            "Natural Language Processing",
            "Computer Vision",
            "SQL",
            "Git",
            "Docker",
        ],
    },

    {
        "role": "Python Developer",
        "category": "Software Development",
        "description": "Develops software applications and backend systems using Python.",
        "required_skills": [
            "Python",
            "SQL",
            "Git",
            "FastAPI",
            "Django",
            "REST APIs",
            "PostgreSQL",
        ],
    },

    {
        "role": "Full Stack Developer",
        "category": "Software Development",
        "description": "Builds complete web applications across frontend and backend technologies.",
        "required_skills": [
            "HTML",
            "CSS",
            "JavaScript",
            "React",
            "Node.js",
            "SQL",
            "Git",
            "REST APIs",
        ],
    },

    {
        "role": "Business Analyst",
        "category": "Business & Analytics",
        "description": "Analyzes business requirements, processes, and data to support organizational decisions.",
        "required_skills": [
            "SQL",
            "Microsoft Excel",
            "Power BI",
            "Data Visualization",
            "Statistics",
            "Data Analysis",
            "Communication",
        ],
    },

    {
        "role": "Data Engineer",
        "category": "Data Engineering",
        "description": "Builds and maintains data pipelines, storage systems, and data processing infrastructure.",
        "required_skills": [
            "Python",
            "SQL",
            "PostgreSQL",
            "Git",
            "Apache Spark",
            "Apache Kafka",
            "Docker",
            "ETL",
        ],
    },
]


def get_all_job_roles() -> list[dict]:
    """
    Return all available job roles.
    """

    return JOB_ROLES


def get_job_role(role_name: str) -> dict | None:
    """
    Find a job role by name.
    """

    normalized_name = role_name.strip().lower()

    for role in JOB_ROLES:
        if role["role"].lower() == normalized_name:
            return role

    return None