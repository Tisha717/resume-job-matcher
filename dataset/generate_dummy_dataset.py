import csv
import random
from datetime import datetime, timedelta

# ---------------- CONFIG ----------------
NUM_USERS = 50
NUM_RECRUITERS = 10
NUM_CANDIDATES = 40
NUM_JOBS = 300
NUM_MATCHES = 100

start_date = datetime(2024, 1, 1)

# ---------------- HELPERS ----------------
def rand_date(days=30):
    return (start_date + timedelta(days=random.randint(0, days))).strftime("%Y-%m-%d %H:%M:%S")

job_roles = [
    "Backend Engineer", "Frontend Engineer", "Full Stack Engineer",
    "Data Analyst", "Data Engineer", "ML Engineer",
    "DevOps Engineer", "QA Automation Engineer",
    "Software Engineer", "Cloud Engineer"
]

skills_map = {
    "Backend Engineer": "Python, FastAPI, Django, PostgreSQL, REST APIs",
    "Frontend Engineer": "React, JavaScript, Material UI, UI Development",
    "Full Stack Engineer": "React, Node.js, Python, APIs, Databases",
    "Data Analyst": "SQL, Python, Pandas, Data Visualization",
    "Data Engineer": "ETL, SQL, Python, Data Pipelines",
    "ML Engineer": "Python, NLP, Machine Learning, Embeddings",
    "DevOps Engineer": "Docker, Kubernetes, CI/CD, AWS",
    "QA Automation Engineer": "Selenium, Python, Automation Testing",
    "Software Engineer": "Python, Java, Software Development",
    "Cloud Engineer": "AWS, Azure, Cloud Infrastructure"
}

# ---------------- USERS ----------------
users = []
user_id = 1

for i in range(NUM_RECRUITERS):
    users.append([user_id, f"recruiter{i+1}@test.com", "hashed_pw", "recruiter", rand_date()])
    user_id += 1

for i in range(NUM_CANDIDATES):
    users.append([user_id, f"candidate{i+1}@test.com", "hashed_pw", "candidate", rand_date()])
    user_id += 1

# ---------------- JOBS ----------------
jobs = []
for job_id in range(1, NUM_JOBS + 1):
    role = random.choice(job_roles)
    recruiter_id = random.randint(1, NUM_RECRUITERS)
    jobs.append([
        job_id,
        recruiter_id,
        role,
        skills_map[role],
        rand_date()
    ])

# ---------------- RESUMES ----------------
resumes = []
resume_id = 1
candidate_start_id = NUM_RECRUITERS + 1

for user_id in range(candidate_start_id, candidate_start_id + NUM_CANDIDATES):
    role = random.choice(job_roles)
    resumes.append([
        resume_id,
        user_id,
        f"Professional with experience in {skills_map[role]}.",
        rand_date()
    ])
    resume_id += 1

# ---------------- MATCH SCORES ----------------
match_scores = []
for match_id in range(1, NUM_MATCHES + 1):
    resume_id = random.randint(1, NUM_CANDIDATES)
    job_id = random.randint(1, NUM_JOBS)
    score = round(random.uniform(0.35, 0.95), 2)
    category = (
        "Strong" if score >= 0.8 else
        "Good" if score >= 0.6 else
        "Partial" if score >= 0.4 else
        "Weak"
    )
    match_scores.append([
        match_id,
        resume_id,
        job_id,
        score,
        category,
        rand_date()
    ])

# ---------------- WRITE CSVs ----------------
with open("output/users.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["id", "email", "password_hash", "role", "created_at"])
    writer.writerows(users)

with open("output/jobs.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["id", "recruiter_id", "title", "description", "created_at"])
    writer.writerows(jobs)

with open("output/resumes.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["id", "user_id", "raw_text", "created_at"])
    writer.writerows(resumes)

with open("output/match_scores.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["id", "resume_id", "job_id", "score", "category", "created_at"])
    writer.writerows(match_scores)

print("CSV files generated successfully.")
