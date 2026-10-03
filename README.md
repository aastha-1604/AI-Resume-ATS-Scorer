# AI Resume ATS Scorer

An AI-powered resume analysis application that compares a candidate's resume with a job description using skill matching, semantic similarity, ATS scoring, and LLM-based recommendations.

## Try the Deployed Application

🔗 **Live Application:** [Try AI Resume ATS Scorer](PASTE_YOUR_STREAMLIT_APP_LINK_HERE)

---

## Project Overview

The AI Resume ATS Scorer helps users evaluate how well their resume matches a particular job description.

Users can upload a **PDF or DOCX resume**, paste the target **job description**, and receive:

- ATS Score
- Matched Skills
- Missing Skills
- Semantic Similarity Score
- Score Breakdown
- AI-generated Resume Improvement Recommendations

---

## Features

- Upload resumes in PDF or DOCX format
- Extract and preprocess resume text
- Identify skills from resume and job description
- Detect matched and missing skills
- Calculate ATS compatibility score
- Measure semantic similarity between resume and job description
- Generate personalized improvement recommendations using Groq LLM
- Interactive Streamlit user interface
- FastAPI-based backend API
- Input validation and API error handling

---

## Tech Stack

**Programming Language**
- Python

**Frontend**
- Streamlit

**Backend**
- FastAPI
- Uvicorn

**NLP & AI**
- spaCy
- Sentence Transformers
- Groq LLM

**Other Libraries**
- scikit-learn
- NumPy
- Requests
- PyPDF2
- python-docx
- python-dotenv
- python-multipart

---

## Project Architecture

```text
User
  │
  ▼
Streamlit Frontend
  │
  │ Resume + Job Description
  ▼
FastAPI Backend
  │
  ▼
Resume Parsing
  │
  ▼
Text Preprocessing
  │
  ▼
Skill Extraction
  │
  ▼
Skill Matching
  │
  ▼
Semantic Similarity
  │
  ▼
ATS Score Calculation
  │
  ▼
Groq LLM Recommendations
  │
  ▼
JSON Response
  │
  ▼
Streamlit Dashboard
