# ---------------------------------------------------------
# SKILLS DATABASE
# ---------------------------------------------------------

SKILLS = [

    # Programming
    "python",
    "java",
    "c++",
    "javascript",

    # Data Analysis
    "sql",
    "excel",
    "power bi",
    "tableau",

    # Python Libraries
    "pandas",
    "numpy",
    "matplotlib",
    "seaborn",
    "plotly",

    # Machine Learning
    "machine learning",
    "deep learning",
    "scikit-learn",
    "xgboost",
    "random forest",

    # Statistics
    "statistics",
    "hypothesis testing",
    "a/b testing",

    # Databases
    "postgresql",
    "mysql",
    "mongodb",

    # Backend
    "fastapi",
    "flask",
    "django",

    # AI / NLP
    "nlp",
    "natural language processing",
    "llm",
    "langchain",
    "langgraph",
    "rag",
    "sentence transformers",

    # Cloud / Deployment
    "aws",
    "azure",
    "docker",
    "kubernetes",

    # BI / Business
    "data visualization",
    "dashboard",
    "business analysis",
    "data analysis"
]


# ---------------------------------------------------------
# NORMALIZE TEXT
# ---------------------------------------------------------

def normalize_text(text: str) -> str:

    return text.lower()


# ---------------------------------------------------------
# EXTRACT SKILLS
# ---------------------------------------------------------

def extract_skills(text: str) -> list:
    """
    Extract known skills from text.
    """

    text = normalize_text(text)

    found_skills = []

    for skill in SKILLS:

        if skill in text:

            found_skills.append(
                skill
            )

    return sorted(
        list(set(found_skills))
    )


# ---------------------------------------------------------
# COMPARE RESUME AND JD SKILLS
# ---------------------------------------------------------

def compare_skills(
    resume_text: str,
    job_description: str
) -> dict:

    resume_skills = extract_skills(
        resume_text
    )

    job_skills = extract_skills(
        job_description
    )

    matched_skills = []

    missing_skills = []

    for skill in job_skills:

        if skill in resume_skills:

            matched_skills.append(
                skill
            )

        else:

            missing_skills.append(
                skill
            )

    return {

        "resume_skills":
            resume_skills,

        "job_skills":
            job_skills,

        "matched_skills":
            matched_skills,

        "missing_skills":
            missing_skills
    }


# ---------------------------------------------------------
# CALCULATE SKILL MATCH SCORE
# ---------------------------------------------------------

def calculate_skill_match_score(
    resume_text: str,
    job_description: str
) -> float:

    comparison = compare_skills(
        resume_text,
        job_description
    )

    job_skills = comparison[
        "job_skills"
    ]

    matched_skills = comparison[
        "matched_skills"
    ]

    # Avoid division by zero

    if len(job_skills) == 0:

        return 0.0

    score = (
        len(matched_skills)
        /
        len(job_skills)
    ) * 100

    return round(
        score,
        2
    )


# ---------------------------------------------------------
# TEST CODE
# ---------------------------------------------------------

if __name__ == "__main__":

    resume_text = """
    Data Analyst with experience in Python,
    SQL, Excel, Power BI, Pandas and NumPy.

    Built dashboards and performed data analysis
    using Python and Power BI.
    """

    job_description = """
    We are hiring a Data Analyst.

    Required skills include Python, SQL,
    Excel, Tableau, Power BI and Statistics.

    Experience with dashboards and data visualization
    is preferred.
    """

    result = compare_skills(
        resume_text,
        job_description
    )

    score = calculate_skill_match_score(
        resume_text,
        job_description
    )

    print("\n==============================")
    print("RESUME SKILLS")
    print("==============================")

    print(
        result["resume_skills"]
    )

    print("\n==============================")
    print("JOB REQUIRED SKILLS")
    print("==============================")

    print(
        result["job_skills"]
    )

    print("\n==============================")
    print("MATCHED SKILLS")
    print("==============================")

    print(
        result["matched_skills"]
    )

    print("\n==============================")
    print("MISSING SKILLS")
    print("==============================")

    print(
        result["missing_skills"]
    )

    print("\n==============================")
    print("SKILL MATCH SCORE")
    print("==============================")

    print(
        f"{score}%"
    )