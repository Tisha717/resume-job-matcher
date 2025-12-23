from text_cleaner import clean_text
from skill_extractor import extract_skills
from scorer import compute_skill_score, categorize_score
from embedding import compute_semantic_similarity

resume_text = """
Backend engineer with experience in Python, FastAPI,
PostgreSQL and REST APIs.
"""

job_text = """
Looking for a Backend Engineer with Python, FastAPI,
Docker and PostgreSQL experience.
"""

resume_clean = clean_text(resume_text)
job_clean = clean_text(job_text)

# Skill matching
resume_skills = extract_skills(resume_clean)
job_skills = extract_skills(job_clean)
skill_score = compute_skill_score(resume_skills, job_skills)

# Semantic matching
semantic_score = compute_semantic_similarity(resume_clean, job_clean)

# Final score (weighted)
final_score = round(
    0.7 * semantic_score + 0.3 * skill_score,
    2
)

category = categorize_score(final_score)

print("Resume Skills:", resume_skills)
print("Job Skills:", job_skills)
print("Skill Score:", skill_score)
print("Semantic Score:", semantic_score)
print("Final Score:", final_score)
print("Category:", category)
