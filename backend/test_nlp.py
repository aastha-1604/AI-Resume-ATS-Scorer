from backend.services.text_preprocessor import (
    preprocess_text
)

from backend.services.skill_extractor import (
    compare_skills,
    calculate_skill_match_score
)

from backend.services.semantic_matcher import (
    calculate_semantic_similarity
)


# ---------------------------------------------------------
# SAMPLE RESUME
# ---------------------------------------------------------

resume_text = """
Data Analyst with experience in Python,
SQL, Excel, Power BI, Pandas and NumPy.

Built interactive dashboards and analyzed
customer datasets to identify trends.

Developed machine learning models for
customer churn prediction.
"""


# ---------------------------------------------------------
# SAMPLE JOB DESCRIPTION
# ---------------------------------------------------------

job_description = """
We are hiring a Data Analyst.

The candidate should have experience in
Python, SQL, Excel, Tableau and Power BI.

Experience in customer analytics,
data visualization, statistics and
machine learning is preferred.
"""


# ---------------------------------------------------------
# PREPROCESSING
# ---------------------------------------------------------

processed_resume = preprocess_text(
    resume_text
)

processed_job_description = preprocess_text(
    job_description
)


# ---------------------------------------------------------
# SKILL COMPARISON
# ---------------------------------------------------------

skill_result = compare_skills(
    resume_text,
    job_description
)


# ---------------------------------------------------------
# SKILL MATCH SCORE
# ---------------------------------------------------------

skill_score = calculate_skill_match_score(
    resume_text,
    job_description
)


# ---------------------------------------------------------
# SEMANTIC MATCH SCORE
# ---------------------------------------------------------

semantic_score = calculate_semantic_similarity(
    resume_text,
    job_description
)


# ---------------------------------------------------------
# OUTPUT
# ---------------------------------------------------------

print("\n==============================")
print("PROCESSED RESUME")
print("==============================\n")

print(processed_resume)


print("\n==============================")
print("PROCESSED JOB DESCRIPTION")
print("==============================\n")

print(processed_job_description)


print("\n==============================")
print("MATCHED SKILLS")
print("==============================\n")

print(
    skill_result["matched_skills"]
)


print("\n==============================")
print("MISSING SKILLS")
print("==============================\n")

print(
    skill_result["missing_skills"]
)


print("\n==============================")
print("SKILL MATCH SCORE")
print("==============================\n")

print(
    f"{skill_score}%"
)


print("\n==============================")
print("SEMANTIC MATCH SCORE")
print("==============================\n")

print(
    f"{semantic_score}%"
)