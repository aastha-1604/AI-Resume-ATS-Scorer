import os

from dotenv import load_dotenv
from groq import Groq


# ---------------------------------------------------------
# LOAD ENVIRONMENT VARIABLES
# ---------------------------------------------------------

load_dotenv()


# ---------------------------------------------------------
# GET GROQ API KEY
# ---------------------------------------------------------

api_key = os.getenv(
    "GROQ_API_KEY"
)


if not api_key:

    raise ValueError(
        "GROQ_API_KEY not found in .env file"
    )


# ---------------------------------------------------------
# CREATE GROQ CLIENT
# ---------------------------------------------------------

client = Groq(
    api_key=api_key
)


# ---------------------------------------------------------
# GENERATE AI RECOMMENDATIONS
# ---------------------------------------------------------

def generate_ai_recommendations(
    resume_text: str,
    job_description: str,
    missing_skills: list,
    ats_scores: dict
) -> str:

    prompt = f"""
You are an expert resume reviewer.

Analyze the resume against the job description.

RESUME:
{resume_text}

JOB DESCRIPTION:
{job_description}

MISSING SKILLS:
{", ".join(missing_skills)}

ATS SCORES:
Skill Match: {ats_scores["skill_score"]}
Keyword Match: {ats_scores["keyword_score"]}
Semantic Match: {ats_scores["semantic_score"]}
Structure Score: {ats_scores["structure_score"]}
Content Quality: {ats_scores["content_score"]}
Final ATS Score: {ats_scores["final_ats_score"]}

Give concise and practical recommendations.

Return recommendations under these headings:

1. Missing Skills
2. Resume Content Improvements
3. Keyword Improvements
4. Structure Improvements
5. Final Recommendations

Do not invent experience or skills that the candidate
does not actually have.

Keep the recommendations concise.
"""

    response = client.chat.completions.create(

        model="openai/gpt-oss-120b",

        messages=[
            {
                "role": "system",
                "content":
                    "You are an expert ATS resume reviewer."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],

        temperature=0.3
    )

    recommendations = (
        response
        .choices[0]
        .message
        .content
    )

    return recommendations


# ---------------------------------------------------------
# TEST CODE
# ---------------------------------------------------------

if __name__ == "__main__":

    sample_resume = """
    Data Analyst skilled in Python,
    SQL, Excel and Power BI.

    Built dashboards and analyzed
    customer datasets.
    """

    sample_job_description = """
    Looking for a Data Analyst with
    Python, SQL, Tableau, Excel,
    statistics and visualization skills.
    """

    sample_missing_skills = [
        "tableau",
        "statistics"
    ]

    sample_scores = {

        "skill_score": 65,

        "keyword_score": 60,

        "semantic_score": 78,

        "structure_score": 80,

        "content_score": 70,

        "final_ats_score": 70.5
    }

    result = generate_ai_recommendations(
        sample_resume,
        sample_job_description,
        sample_missing_skills,
        sample_scores
    )

    print("\n==============================")
    print("AI RECOMMENDATIONS")
    print("==============================\n")

    print(result)