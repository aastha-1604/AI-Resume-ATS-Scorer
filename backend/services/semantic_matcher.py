from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


# ---------------------------------------------------------
# LOAD SENTENCE TRANSFORMER MODEL
# ---------------------------------------------------------

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


# ---------------------------------------------------------
# CALCULATE SEMANTIC SIMILARITY
# ---------------------------------------------------------

def calculate_semantic_similarity(
    resume_text: str,
    job_description: str
) -> float:
    """
    Compare resume and job description based on meaning.

    Returns similarity score from 0 to 100.
    """

    # Convert both texts into numerical embeddings
    embeddings = model.encode(
        [
            resume_text,
            job_description
        ]
    )

    resume_embedding = embeddings[0]
    job_embedding = embeddings[1]

    # Calculate cosine similarity
    similarity = cosine_similarity(
        [resume_embedding],
        [job_embedding]
    )[0][0]

    # Convert 0-1 score into percentage
    similarity_percentage = (
        float(similarity) * 100
    )

    return round(
        similarity_percentage,
        2
    )


# ---------------------------------------------------------
# TEST CODE
# ---------------------------------------------------------

if __name__ == "__main__":

    resume_text = """
    Data Analyst with experience in Python,
    SQL, Power BI and Excel.

    Built interactive dashboards and analyzed
    customer data to identify business trends.

    Developed machine learning models for
    customer churn prediction.
    """

    job_description = """
    We are hiring a Data Analyst with experience
    in Python and SQL.

    The candidate should have experience in
    data visualization, dashboard development,
    customer analytics and machine learning.
    """

    score = calculate_semantic_similarity(
        resume_text,
        job_description
    )

    print("\n==============================")
    print("SEMANTIC MATCH SCORE")
    print("==============================\n")

    print(f"{score}%")