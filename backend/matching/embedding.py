from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load once (IMPORTANT)
model = SentenceTransformer("all-MiniLM-L6-v2")


def compute_semantic_similarity(resume_text: str, job_text: str) -> float:
    embeddings = model.encode([resume_text, job_text])
    similarity = cosine_similarity(
        [embeddings[0]],
        [embeddings[1]]
    )[0][0]

    return round(float(similarity), 2)

print("Loading sentence transformer model...")
model = SentenceTransformer("all-MiniLM-L6-v2")
print("Model loaded.")
