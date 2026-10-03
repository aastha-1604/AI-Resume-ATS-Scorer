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
