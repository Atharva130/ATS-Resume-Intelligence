# 🏆 ATS-Inspired Resume Intelligence & Ranking System

A **full-stack, ATS-inspired resume intelligence system** that parses resumes (PDF/DOCX), extracts structured information using NLP, and ranks resumes against a given Job Description (JD) using an **explainable, weighted ATS scoring mechanism**.

This project mimics how **real Applicant Tracking Systems (ATS)** evaluate candidates by combining **rule-based logic, NLP techniques, and classical machine learning**, deployed using a REST-based backend and a clean frontend UI.

---

## 🚀 Features

- 📂 Upload resumes in **PDF or DOCX**
- 🧠 Extract structured information:
  - Email
  - Phone Number
  - Years of Experience
  - Skills
- 🔀 Hybrid NLP pipeline:
  - Regex for deterministic fields
  - SpaCy NLP for skill extraction
- 📊 Job-specific **ATS relevance score (0–100)**
- 🔍 Semantic similarity between Resume & Job Description (TF-IDF + cosine similarity)
- 🖥️ Clean frontend UI (no Streamlit)
- 🌐 RESTful Flask backend
- ☁️ Deployment-ready architecture

---

## 🏗️ System Architecture

Resume (PDF/DOCX)
│
▼
Text Extraction (pdfplumber / python-docx)
│
▼
Regex + NLP (SpaCy)
│
▼
Feature Extraction
│
▼
Resume ↔ Job Description Comparison
│
▼
Weighted ATS Scoring Engine
│
▼
Final ATS Score (0–100)


---

## 🛠️ Tech Stack

### Backend
- Python
- Flask (REST API)
- SpaCy (NLP)
- Regex
- Scikit-learn (TF-IDF, Cosine Similarity)
- pdfplumber (PDF parsing)
- python-docx (DOCX parsing)
- Gunicorn (Production server)

### Frontend
- HTML
- CSS
- JavaScript (Fetch API)

### Deployment
- Backend: Render
- Frontend: Netlify

---

## 📊 ATS Scoring Logic

The ATS score is **fully explainable and rule-based**, inspired by real-world ATS systems:

| Component            | Weight |
|----------------------|--------|
| Skill Match          | 40%    |
| Experience Match     | 30%    |
| Semantic Similarity  | 10%    |
| Baseline / Education | 20%    |

> ⚠️ No black-box deep learning is used for final decision-making.  
> The system prioritizes **interpretability, robustness, and realism**.

---

## 🧠 NLP & ML Concepts Used

- Resume document parsing
- Regular Expressions for structured data extraction
- Natural Language Processing (SpaCy)
- Skill keyword matching
- TF-IDF Vectorization
- Cosine Similarity
- Explainable rule-based scoring systems

---

## 🖥️ How to Run Locally

 1️⃣ Clone the repository
```bash
git clone https://github.com/Atharva130/ATS-Resume-Intelligence.git
cd ATS-Resume-Intelligence

2️⃣ Create & activate virtual environment
python -m venv venv
venv\Scripts\activate   # Windows

3️⃣ Install dependencies
pip install -r requirements.txt
python -m spacy download en_core_web_sm

4️⃣ Run backend
python backend/app.py

5️⃣ Open frontend

Open frontend/index.html using Live Server in VS Code.

🌐 API Endpoint
POST /analyze

Request

Resume file (PDF/DOCX)

Job Description text

Response

{
  "email": "example@gmail.com",
  "phone": "+91 9876543210",
  "experience": 2,
  "skills": ["python", "machine learning", "flask"],
  "ats_score": 74.5
}

🎯 Why This Project Stands Out

Implements ATS-style ranking, not just resume parsing

Job-specific relevance scoring

End-to-end system (backend + frontend + deployment)

Explainable logic instead of black-box ML

Highly relevant to AI, NLP, and HR-tech systems

🔮 Future Enhancements

Skill synonym normalization using embeddings

Education & degree relevance scoring

Configurable ATS weight sliders

Resume improvement suggestions

Multi-resume ranking

👤 Author

Atharva Rahate
B.Tech – Computer Technology
Interests: AI, Machine Learning, NLP, Full-Stack Development