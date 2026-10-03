import os
import shutil
import uuid

from fastapi import (
    FastAPI,
    UploadFile,
    File,
    Form,
    HTTPException
)

from fastapi.middleware.cors import CORSMiddleware

from backend.services.resume_parser import (
    extract_resume_text
)

from backend.services.skill_extractor import (
    compare_skills
)

from backend.services.ats_scorer import (
    calculate_ats_score
)

from backend.services.ai_recommendation import (
    generate_ai_recommendations
)


# ---------------------------------------------------------
# CREATE FASTAPI APPLICATION
# ---------------------------------------------------------

app = FastAPI(
    title="AI Resume ATS Scorer",
    version="1.0"
)


# ---------------------------------------------------------
# CORS
# ---------------------------------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ---------------------------------------------------------
# UPLOAD DIRECTORY
# ---------------------------------------------------------

UPLOAD_DIR = "data"

os.makedirs(
    UPLOAD_DIR,
    exist_ok=True
)


# ---------------------------------------------------------
# HOME ROUTE
# ---------------------------------------------------------

@app.get("/")
def home():

    return {
        "message": "AI Resume ATS Scorer API is running"
    }


# ---------------------------------------------------------
# ANALYZE RESUME
# ---------------------------------------------------------

@app.post("/analyze")
async def analyze_resume(
    resume: UploadFile = File(...),
    job_description: str = Form(...)
):

    # -----------------------------------------------------
    # 1. VALIDATE FILE TYPE
    # -----------------------------------------------------

    allowed_extensions = (
        ".pdf",
        ".docx"
    )

    original_filename = (
        resume.filename or "resume"
    )

    file_extension = os.path.splitext(
        original_filename
    )[1].lower()

    if file_extension not in allowed_extensions:

        raise HTTPException(
            status_code=400,
            detail="Only PDF and DOCX files are supported."
        )


    # -----------------------------------------------------
    # 2. VALIDATE JOB DESCRIPTION
    # -----------------------------------------------------

    if not job_description.strip():

        raise HTTPException(
            status_code=400,
            detail="Job description cannot be empty."
        )


    # -----------------------------------------------------
    # 3. GENERATE UNIQUE FILE NAME
    # -----------------------------------------------------

    unique_filename = (
        f"{uuid.uuid4()}{file_extension}"
    )

    file_path = os.path.join(
        UPLOAD_DIR,
        unique_filename
    )


    # -----------------------------------------------------
    # 4. SAVE UPLOADED RESUME
    # -----------------------------------------------------

    try:

        with open(
            file_path,
            "wb"
        ) as buffer:

            shutil.copyfileobj(
                resume.file,
                buffer
            )


        # -------------------------------------------------
        # 5. EXTRACT RESUME TEXT
        # -------------------------------------------------

        resume_text = extract_resume_text(
            file_path
        )


        if not resume_text.strip():

            raise HTTPException(
                status_code=400,
                detail=(
                    "No readable text was found "
                    "in the resume."
                )
            )


        # -------------------------------------------------
        # 6. SKILL ANALYSIS
        # -------------------------------------------------

        skill_result = compare_skills(
            resume_text,
            job_description
        )


        # -------------------------------------------------
        # 7. ATS SCORE
        # -------------------------------------------------

        ats_scores = calculate_ats_score(
            resume_text,
            job_description
        )


        # -------------------------------------------------
        # 8. AI RECOMMENDATIONS
        # -------------------------------------------------

        recommendations = (
            generate_ai_recommendations(
                resume_text,
                job_description,
                skill_result["missing_skills"],
                ats_scores
            )
        )


        # -------------------------------------------------
        # 9. RETURN COMPLETE RESULT
        # -------------------------------------------------

        return {

            "filename":
                original_filename,

            "ats_score":
                ats_scores["final_ats_score"],

            "score_breakdown": {

                "skill_match":
                    ats_scores["skill_score"],

                "keyword_match":
                    ats_scores["keyword_score"],

                "semantic_match":
                    ats_scores["semantic_score"],

                "resume_structure":
                    ats_scores["structure_score"],

                "content_quality":
                    ats_scores["content_score"]
            },

            "skills": {

                "resume_skills":
                    skill_result["resume_skills"],

                "job_skills":
                    skill_result["job_skills"],

                "matched_skills":
                    skill_result["matched_skills"],

                "missing_skills":
                    skill_result["missing_skills"]
            },

            "ai_recommendations":
                recommendations
        }


    # -----------------------------------------------------
    # HANDLE KNOWN FASTAPI ERRORS
    # -----------------------------------------------------

    except HTTPException:

        raise


    # -----------------------------------------------------
    # HANDLE UNEXPECTED ERRORS
    # -----------------------------------------------------

    except Exception as error:

        raise HTTPException(
            status_code=500,
            detail=str(error)
        )


    # -----------------------------------------------------
    # DELETE TEMPORARY FILE
    # -----------------------------------------------------

    finally:

        try:

            await resume.close()

        except Exception:

            pass


        if os.path.exists(
            file_path
        ):

            try:

                os.remove(
                    file_path
                )

            except OSError:

                pass