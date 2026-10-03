import re

from backend.services.skill_extractor import (
    calculate_skill_match_score
)

from backend.services.semantic_matcher import (
    calculate_semantic_similarity
)


# ---------------------------------------------------------
# KEYWORD MATCH SCORE
# ---------------------------------------------------------

def calculate_keyword_match_score(
    resume_text: str,
    job_description: str
) -> float:

    resume_words = set(
        re.findall(
            r"\b[a-zA-Z]+\b",
            resume_text.lower()
        )
    )

    jd_words = set(
        re.findall(
            r"\b[a-zA-Z]+\b",
            job_description.lower()
        )
    )

    # Remove very common words
    common_words = {
        "the",
        "and",
        "a",
        "an",
        "is",
        "are",
        "of",
        "to",
        "in",
        "for",
        "with",
        "on",
        "as",
        "at",
        "by",
        "be"
    }

    resume_words = resume_words - common_words
    jd_words = jd_words - common_words

    if len(jd_words) == 0:
        return 0.0

    matched_keywords = (
        resume_words.intersection(
            jd_words
        )
    )

    score = (
        len(matched_keywords)
        /
        len(jd_words)
    ) * 100

    return round(
        score,
        2
    )


# ---------------------------------------------------------
# RESUME STRUCTURE SCORE
# ---------------------------------------------------------

def calculate_structure_score(
    resume_text: str
) -> float:

    text = resume_text.lower()

    important_sections = [
        "education",
        "experience",
        "skills",
        "projects",
        "summary"
    ]

    found_sections = 0

    for section in important_sections:

        if section in text:
            found_sections += 1

    score = (
        found_sections
        /
        len(important_sections)
    ) * 100

    return round(
        score,
        2
    )


# ---------------------------------------------------------
# CONTENT QUALITY SCORE
# ---------------------------------------------------------

def calculate_content_quality_score(
    resume_text: str
) -> float:

    score = 0

    text = resume_text.lower()

    # 1. Resume length
    word_count = len(
        resume_text.split()
    )

    if 200 <= word_count <= 1000:
        score += 30

    elif 100 <= word_count < 200:
        score += 20

    elif word_count > 1000:
        score += 20

    # 2. Quantified achievements
    numbers = re.findall(
        r"\d+[%+]?",
        resume_text
    )

    if len(numbers) >= 3:
        score += 30

    elif len(numbers) >= 1:
        score += 15

    # 3. Action verbs
    action_verbs = [
        "developed",
        "built",
        "created",
        "analyzed",
        "implemented",
        "improved",
        "managed",
        "designed",
        "optimized",
        "led",
        "increased",
        "reduced"
    ]

    action_count = 0

    for verb in action_verbs:

        if verb in text:
            action_count += 1

    if action_count >= 4:
        score += 25

    elif action_count >= 2:
        score += 15

    elif action_count >= 1:
        score += 10

    # 4. Contact information
    email_pattern = r"[\w\.-]+@[\w\.-]+"

    if re.search(
        email_pattern,
        resume_text
    ):
        score += 15

    return min(
        float(score),
        100.0
    )


# ---------------------------------------------------------
# FINAL ATS SCORE
# ---------------------------------------------------------

def calculate_ats_score(
    resume_text: str,
    job_description: str
) -> dict:

    skill_score = (
        calculate_skill_match_score(
            resume_text,
            job_description
        )
    )

    keyword_score = (
        calculate_keyword_match_score(
            resume_text,
            job_description
        )
    )

    semantic_score = (
        calculate_semantic_similarity(
            resume_text,
            job_description
        )
    )

    structure_score = (
        calculate_structure_score(
            resume_text
        )
    )

    content_score = (
        calculate_content_quality_score(
            resume_text
        )
    )

    final_score = (
        skill_score * 0.30
        +
        keyword_score * 0.20
        +
        semantic_score * 0.25
        +
        structure_score * 0.15
        +
        content_score * 0.10
    )

    return {
        "skill_score":
            round(skill_score, 2),

        "keyword_score":
            round(keyword_score, 2),

        "semantic_score":
            round(semantic_score, 2),

        "structure_score":
            round(structure_score, 2),

        "content_score":
            round(content_score, 2),

        "final_ats_score":
            round(final_score, 2)
    }


# ---------------------------------------------------------
# TEST CODE
# ---------------------------------------------------------

if __name__ == "__main__":

    resume_text = """
    Aastha Singh
    aastha@example.com

    Summary
    Data Analyst with experience in Python,
    SQL, Excel and Power BI.

    Skills
    Python, SQL, Excel, Power BI,
    Pandas, NumPy, Machine Learning

    Experience
    Developed dashboards using Power BI.
    Analyzed 12000+ sales transactions.
    Improved reporting efficiency by 30%.

    Projects
    Built a customer churn prediction model
    using Python and machine learning.

    Education
    B.Tech Electronics and Communication Engineering
    """

    job_description = """
    We are looking for a Data Analyst
    with experience in Python, SQL,
    Excel, Tableau and Power BI.

    Candidates should have strong experience
    in data visualization, statistics,
    dashboard development and machine learning.
    """

    result = calculate_ats_score(
        resume_text,
        job_description
    )

    print("\n==============================")
    print("ATS SCORE BREAKDOWN")
    print("==============================\n")

    print(
        "Skill Match:",
        result["skill_score"]
    )

    print(
        "Keyword Match:",
        result["keyword_score"]
    )

    print(
        "Semantic Match:",
        result["semantic_score"]
    )

    print(
        "Structure:",
        result["structure_score"]
    )

    print(
        "Content Quality:",
        result["content_score"]
    )

    print("\n==============================")
    print("FINAL ATS SCORE")
    print("==============================\n")

    print(
        result["final_ats_score"]
    )