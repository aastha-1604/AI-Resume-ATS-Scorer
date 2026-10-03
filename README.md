# 🤖 AI Resume ATS Scorer

An AI-powered resume analysis application that compares a candidate's resume with a job description using skill matching, semantic similarity, ATS scoring, and LLM-based recommendations.

---

## 📌 Project Overview

The **AI Resume ATS Scorer** helps users evaluate how well their resume matches a particular job description.

The application allows users to:

- Upload a resume in **PDF or DOCX format**
- Paste a target **Job Description**
- Calculate an **ATS Score**
- Identify **Matched Skills**
- Identify **Missing Skills**
- Measure **Semantic Similarity**
- View a detailed **Score Breakdown**
- Receive **AI-generated resume improvement recommendations**

---

## ✨ Key Features

- 📄 PDF and DOCX resume upload
- 🔍 Resume text extraction and preprocessing
- 🧠 Skill extraction using NLP
- ✅ Matched skill identification
- ❌ Missing skill identification
- 📊 ATS compatibility scoring
- 🔗 Semantic similarity analysis
- 🤖 AI-powered recommendations using Groq LLM
- ⚡ FastAPI-based backend
- 🎨 Interactive Streamlit frontend
- 🛡️ Input validation and API error handling

---

## 🛠️ Tech Stack

### Programming
- Python

### Frontend
- Streamlit

### Backend
- FastAPI
- Uvicorn

### NLP & Machine Learning
- spaCy
- Sentence Transformers
- Scikit-learn

### Generative AI
- Groq API
- Llama

### Resume Processing
- PyPDF2
- python-docx

### API Communication
- Requests
- REST API
- Multipart Form Data

---

## 🏗️ Project Architecture

```text
User
 │
 ▼
Streamlit Frontend
 │
 │ Resume + Job Description
 │
 ▼
FastAPI Backend
 │
 ▼
Resume Parser
 │
 ▼
Text Preprocessing
 │
 ▼
Skill Extraction
 │
 ├───────────────┐
 ▼               ▼
ATS Scoring   Semantic Matching
 │               │
 └───────┬───────┘
         ▼
    Groq LLM
         │
         ▼
AI Recommendations
         │
         ▼
JSON Response
         │
         ▼
Streamlit Dashboard
```

---

## 🔄 Application Workflow

```text
Upload Resume
      ↓
Enter Job Description
      ↓
Streamlit sends POST request
      ↓
FastAPI receives Resume + JD
      ↓
Resume text is extracted
      ↓
Text is preprocessed
      ↓
Skills are extracted
      ↓
Resume skills are compared with JD skills
      ↓
Matched and Missing Skills are identified
      ↓
ATS Score is calculated
      ↓
Semantic Similarity is calculated
      ↓
Groq LLM generates recommendations
      ↓
FastAPI returns JSON response
      ↓
Streamlit displays results
```

---

## 📂 Project Structure

```text
AI-Resume-ATS-Scorer/
│
├── backend/
│   │
│   ├── main.py
│   │
│   └── services/
│       ├── ats_scorer.py
│       ├── resume_parser.py
│       ├── semantic_matcher.py
│       ├── skill_extractor.py
│       └── text_preprocessor.py
│
├── frontend/
│   └── app.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/AI-Resume-ATS-Scorer.git
```

Move inside the project folder:

```bash
cd AI-Resume-ATS-Scorer
```

---

### 2. Create a Virtual Environment

```bash
python -m venv ats_env
```

Activate it on Windows:

```bash
ats_env\Scripts\activate
```

For macOS/Linux:

```bash
source ats_env/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Create Environment File

Create a `.env` file in the root directory:

```text
.env
```

Add your Groq API key:

```env
GROQ_API_KEY=your_groq_api_key
```

Do not upload the `.env` file to GitHub.

---

## ▶️ Run the Application

The application uses two components:

- FastAPI Backend
- Streamlit Frontend

Both need to run while using the application locally.

---

### Step 1: Start FastAPI Backend

Open a terminal in the project folder and run:

```bash
uvicorn backend.main:app --reload
```

The backend will run at:

```text
http://127.0.0.1:8000
```

FastAPI Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

Keep this terminal running.

---

### Step 2: Start Streamlit Frontend

Open another terminal in the same project folder.

Activate the environment if required:

```bash
ats_env\Scripts\activate
```

Run:

```bash
streamlit run frontend/app.py
```

The application will open at:

```text
http://localhost:8501
```

---

## 💻 How to Use

1. Open the Streamlit application.
2. Upload your resume in **PDF or DOCX format**.
3. Paste the complete **Job Description**.
4. Click **Analyze Resume**.
5. Wait for the analysis to complete.
6. View:
   - ATS Score
   - Matched Skills
   - Missing Skills
   - Score Breakdown
   - AI Recommendations

---

## 🌐 API Endpoint

The main backend endpoint is:

```http
POST /analyze
```

It receives:

```text
resume
job_description
```

The resume is sent as a file using multipart form data.

Example frontend request:

```python
files = {
    "resume": (
        uploaded_file.name,
        uploaded_file.getvalue(),
        uploaded_file.type
    )
}

data = {
    "job_description": job_description
}

response = requests.post(
    API_URL,
    files=files,
    data=data
)
```

---

## 📊 Output

The application returns analysis containing information such as:

```json
{
  "ats_score": 78,
  "matched_skills": [
    "Python",
    "SQL",
    "Machine Learning"
  ],
  "missing_skills": [
    "Docker",
    "AWS"
  ],
  "score_breakdown": {
    "skill_match": 80,
    "semantic_similarity": 76
  },
  "recommendations": "Add relevant missing skills and strengthen measurable project impact."
}
```

---

## 🧠 ATS Analysis

The ATS analysis considers multiple factors including:

```text
Resume Content
      +
Skill Matching
      +
Job Description Relevance
      +
Semantic Similarity
      ↓
ATS Score
```

This provides a more meaningful comparison than simple keyword matching alone.

---

## 🔍 Skill Matching

The system extracts skills from both:

```text
Resume
   ↓
Resume Skills

Job Description
   ↓
Required Skills
```

They are then compared to identify:

```text
Matched Skills
```

and:

```text
Missing Skills
```

This helps candidates understand the skill gap between their resume and the target role.

---

## 🧠 Semantic Similarity

Sentence Transformers are used to understand the contextual similarity between the resume and job description.

This allows the system to compare meaning rather than relying only on exact keyword matches.

```text
Resume Text
       ↓
Sentence Embedding

Job Description
       ↓
Sentence Embedding

       ↓
Cosine Similarity
       ↓
Semantic Match Score
```

---

## 🤖 AI Recommendations

The final analysis is passed to a Groq-hosted LLM to generate improvement suggestions.

The recommendations help users understand:

- Which skills should be highlighted
- Which important skills are missing
- How resume content can better match the JD
- Areas where the resume can be improved

---

## 🔐 Environment Variables

Sensitive information such as API keys is stored using environment variables.

Example:

```env
GROQ_API_KEY=your_api_key
```

The `.env` file is excluded through `.gitignore`.

Example:

```gitignore
.env
ats_env/
__pycache__/
*.pyc
uploads/
```

---

## 🧪 API Testing

The backend can be tested independently using FastAPI Swagger UI.

Start FastAPI:

```bash
uvicorn backend.main:app --reload
```

Then open:

```text
http://127.0.0.1:8000/docs
```

Select:

```text
POST /analyze
```

Upload a resume, enter a job description, and execute the request.

---

## 🌍 Deployment Architecture

```text
User
 │
 ▼
Streamlit Cloud
 │
 ▼
Public FastAPI Backend
 │
 ▼
Resume Processing
 │
 ▼
ATS + Semantic Analysis
 │
 ▼
Groq LLM
 │
 ▼
Results
```

For local development, the frontend API URL can be:

```python
API_URL = "http://127.0.0.1:8000/analyze"
```

For production deployment, replace it with the public backend URL:

```python
API_URL = "https://your-backend-url.com/analyze"
```

---

## ⚠️ Common Errors

### Backend Error 422

A `422` error usually means the frontend field names do not match the fields expected by FastAPI.

For example, if FastAPI expects:

```python
resume: UploadFile = File(...)
```

the Streamlit request must use:

```python
files = {
    "resume": (...)
}
```

and not:

```python
files = {
    "file": (...)
}
```

---

### Backend Connection Error

If Streamlit shows:

```text
Could not connect to the backend
```

make sure FastAPI is running:

```bash
uvicorn backend.main:app --reload
```

---

### Missing Groq API Key

Make sure `.env` contains:

```env
GROQ_API_KEY=your_api_key
```

and that environment variables are loaded inside the backend.

---

## 📈 Future Improvements

- Resume history dashboard
- User authentication
- Multiple resume comparison
- Job-specific resume suggestions
- Resume section scoring
- Downloadable ATS reports
- Cloud database integration
- Additional LLM models

---

## 👩‍💻 Author

**Aastha Singh**

Data Analytics | Product Thinking | AI Enthusiast

### Skills

`Python` `SQL` `FastAPI` `Streamlit` `NLP` `Machine Learning` `Generative AI`

---

## ⭐ Support

If you found this project useful, consider giving the repository a ⭐ on GitHub.
