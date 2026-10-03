# 📄 AI Resume ATS Scorer

An AI-powered resume analysis application that compares a candidate's resume with a job description using **skill matching, semantic similarity, ATS scoring, and LLM-based recommendations**.

The application provides an interactive **Streamlit frontend** connected to a **FastAPI backend**, allowing users to upload a resume, enter a job description, and receive an ATS-style analysis instantly.

---

## 🚀 Features

- 📄 Upload resumes in PDF or DOCX format
- 📝 Paste any job description
- 🎯 Generate an ATS compatibility score
- ✅ Identify matched skills
- ❌ Identify missing skills
- 🧠 Calculate semantic similarity between resume and job description
- 🤖 Generate AI-based resume improvement recommendations using Groq LLM
- 📊 Display score breakdown through an interactive Streamlit interface
- ⚡ FastAPI-based backend API
- 🔐 Environment-based API key management
- 🛡️ Input validation and API error handling

---

## 🛠️ Tech Stack

### Programming Language
- Python

### Frontend
- Streamlit

### Backend
- FastAPI
- Uvicorn

### NLP & AI
- spaCy
- Sentence Transformers
- Groq API

### Resume Processing
- PyPDF2
- python-docx

### API Communication
- Requests
- REST API
- Multipart Form Data

---

## 🔄 Project Workflow

```text
User
 │
 ▼
Streamlit Frontend
 │
 ├── Upload Resume
 └── Enter Job Description
 │
 ▼
POST /analyze
 │
 ▼
FastAPI Backend
 │
 ├── Resume Parsing
 ├── Text Preprocessing
 ├── Skill Extraction
 ├── Skill Matching
 ├── Semantic Similarity
 ├── ATS Score Calculation
 └── Groq LLM Recommendations
 │
 ▼
JSON Response
 │
 ▼
Streamlit Dashboard
 │
 ├── ATS Score
 ├── Matched Skills
 ├── Missing Skills
 ├── Score Breakdown
 └── AI Recommendations
