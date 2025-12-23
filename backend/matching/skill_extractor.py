SKILL_KEYWORDS = [
    "python", "fastapi", "django", "postgresql", "sql",
    "react", "javascript", "material ui",
    "docker", "kubernetes", "aws",
    "nlp", "machine learning", "embeddings",
    "pandas", "data analysis", "etl",
    "selenium", "automation testing"
]

def extract_skills(text: str) -> set:
    text = text.lower()
    found_skills = set()

    for skill in SKILL_KEYWORDS:
        if skill in text:
            found_skills.add(skill)

    return found_skills
