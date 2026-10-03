import streamlit as st
import requests


# ---------------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------------

st.set_page_config(
    page_title="AI Resume ATS Scorer",
    page_icon="📄",
    layout="wide"
)


# ---------------------------------------------------------
# TITLE
# ---------------------------------------------------------

st.title("AI Resume ATS Scorer")

st.write(
    "Upload your resume and paste a job description "
    "to get an ATS score, skill analysis and AI recommendations."
)


# ---------------------------------------------------------
# BACKEND API URL
# ---------------------------------------------------------

API_URL = "http://127.0.0.1:8000/analyze"


# ---------------------------------------------------------
# INPUT SECTION
# ---------------------------------------------------------

st.subheader("Upload Resume")

uploaded_file = st.file_uploader(
    "Choose a PDF or DOCX resume",
    type=["pdf", "docx"]
)


st.subheader("Job Description")

job_description = st.text_area(
    "Paste the job description here",
    height=250,
    placeholder=(
        "Example: We are looking for a Data Analyst "
        "with Python, SQL, Power BI, Tableau..."
    )
)


# ---------------------------------------------------------
# ANALYZE BUTTON
# ---------------------------------------------------------

analyze_button = st.button(
    "Analyze Resume",
    type="primary"
)


# ---------------------------------------------------------
# ANALYSIS
# ---------------------------------------------------------

if analyze_button:

    # Validate resume
    if uploaded_file is None:

        st.warning(
            "Please upload a resume."
        )

    # Validate job description
    elif not job_description.strip():

        st.warning(
            "Please enter a job description."
        )

    else:

        try:

            # ---------------------------------------------
            # PREPARE FILE
            # ---------------------------------------------

            files = {
                "resume": (
                    uploaded_file.name,
                    uploaded_file.getvalue(),
                    uploaded_file.type
                )
            }


            # ---------------------------------------------
            # PREPARE FORM DATA
            # ---------------------------------------------

            data = {
                "job_description":
                    job_description
            }


            # ---------------------------------------------
            # CALL FASTAPI BACKEND
            # ---------------------------------------------

            with st.spinner(
                "Analyzing your resume..."
            ):

                response = requests.post(
                    API_URL,
                    files=files,
                    data=data,
                    timeout=120
                )


            # ---------------------------------------------
            # SUCCESS
            # ---------------------------------------------

            if response.status_code == 200:

                result = response.json()


                # =========================================
                # ATS SCORE
                # =========================================

                st.success(
                    "Resume analysis completed."
                )

                st.divider()

                st.header(
                    "ATS Score"
                )

                ats_score = result[
                    "ats_score"
                ]

                st.metric(
                    label="Overall ATS Score",
                    value=f"{ats_score}/100"
                )


                # =========================================
                # SCORE BREAKDOWN
                # =========================================

                st.subheader(
                    "Score Breakdown"
                )

                scores = result[
                    "score_breakdown"
                ]


                col1, col2, col3 = st.columns(
                    3
                )

                with col1:

                    st.metric(
                        "Skill Match",
                        f'{scores["skill_match"]}%'
                    )

                with col2:

                    st.metric(
                        "Keyword Match",
                        f'{scores["keyword_match"]}%'
                    )

                with col3:

                    st.metric(
                        "Semantic Match",
                        f'{scores["semantic_match"]}%'
                    )


                col4, col5 = st.columns(
                    2
                )

                with col4:

                    st.metric(
                        "Resume Structure",
                        f'{scores["resume_structure"]}%'
                    )

                with col5:

                    st.metric(
                        "Content Quality",
                        f'{scores["content_quality"]}%'
                    )


                # =========================================
                # SKILLS
                # =========================================

                st.divider()

                st.header(
                    "Skills Analysis"
                )

                skills = result[
                    "skills"
                ]


                col1, col2 = st.columns(
                    2
                )


                # -----------------------------------------
                # MATCHED SKILLS
                # -----------------------------------------

                with col1:

                    st.subheader(
                        "Matched Skills"
                    )

                    matched_skills = skills[
                        "matched_skills"
                    ]

                    if matched_skills:

                        for skill in matched_skills:

                            st.write(
                                f"✅ {skill.title()}"
                            )

                    else:

                        st.write(
                            "No matched skills found."
                        )


                # -----------------------------------------
                # MISSING SKILLS
                # -----------------------------------------

                with col2:

                    st.subheader(
                        "Missing Skills"
                    )

                    missing_skills = skills[
                        "missing_skills"
                    ]

                    if missing_skills:

                        for skill in missing_skills:

                            st.write(
                                f"❌ {skill.title()}"
                            )

                    else:

                        st.write(
                            "No major missing skills found."
                        )


                # =========================================
                # ALL RESUME SKILLS
                # =========================================

                st.divider()

                st.subheader(
                    "Skills Detected in Resume"
                )

                resume_skills = skills[
                    "resume_skills"
                ]

                if resume_skills:

                    st.write(
                        ", ".join(
                            [
                                skill.title()
                                for skill in resume_skills
                            ]
                        )
                    )

                else:

                    st.write(
                        "No known skills detected."
                    )


                # =========================================
                # AI RECOMMENDATIONS
                # =========================================

                st.divider()

                st.header(
                    "AI Recommendations"
                )

                recommendations = result[
                    "ai_recommendations"
                ]

                st.markdown(
                    recommendations
                )


            # ---------------------------------------------
            # BACKEND ERROR
            # ---------------------------------------------

            else:

                try:

                    error_message = response.json().get(
                        "detail",
                        "Unknown backend error."
                    )

                except Exception:

                    error_message = (
                        response.text
                    )

                st.error(
                    f"Backend error: {error_message}"
                )


        # -------------------------------------------------
        # CONNECTION ERROR
        # -------------------------------------------------

        except requests.exceptions.ConnectionError:

            st.error(
                "Could not connect to the FastAPI backend. "
                "Make sure it is running on port 8000."
            )


        # -------------------------------------------------
        # TIMEOUT ERROR
        # -------------------------------------------------

        except requests.exceptions.Timeout:

            st.error(
                "The analysis took too long. "
                "Please try again."
            )


        # -------------------------------------------------
        # OTHER ERROR
        # -------------------------------------------------

        except Exception as error:

            st.error(
                f"Something went wrong: {error}"
            )