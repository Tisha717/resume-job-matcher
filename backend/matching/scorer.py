def compute_skill_score(resume_skills: set, job_skills: set) -> float:
    if not job_skills:
        return 0.0

    matched = resume_skills.intersection(job_skills)
    return round(len(matched) / len(job_skills), 2)


def categorize_score(score: float) -> str:
    if score >= 0.8:
        return "Strong"
    elif score >= 0.6:
        return "Good"
    elif score >= 0.4:
        return "Partial"
    return "Weak"
