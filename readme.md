📄 ATS-Inspired Resume Intelligence & Ranking System

A full-stack, ATS-inspired resume intelligence system that parses resumes (PDF/DOCX), extracts structured information using NLP, and ranks candidates against a given Job Description (JD) using an explainable, weighted ATS scoring mechanism.

This project mimics how real Applicant Tracking Systems (ATS) evaluate resumes by combining rule-based logic, NLP techniques, and classical ML, deployed as a RESTful backend with a clean frontend UI.

🚀 Features

📂 Upload resumes in PDF or DOCX

🧠 Extract structured information:

Email

Phone number

Years of experience

Skills

🧩 Hybrid NLP pipeline:

Regex for deterministic fields

SpaCy NLP for skill extraction

📊 Job-specific ATS relevance score (0–100)

🔍 Semantic similarity between Resume & JD (TF-IDF + cosine similarity)

🖥️ Clean frontend UI (no Streamlit)

🌐 REST-based Flask backend

☁️ Deployment-ready architecture

🏗️ System Architecture
Resume (PDF/DOCX) ──► Text Extraction
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
                    Final ATS Score

🛠️ Tech Stack
Backend

Python

Flask (REST API)

SpaCy (NLP)

Regex

Scikit-learn (TF-IDF, cosine similarity)

pdfplumber (PDF parsing)

python-docx (DOCX parsing)

Gunicorn (production server)

Frontend

HTML

CSS

JavaScript (Fetch API)

Deployment

Backend: Render

Frontend: Netlify (static hosting)

📊 ATS Scoring Logic

The final ATS score is explainable and weighted, inspired by real ATS systems:

Component	Weight
Skill Match	40%
Experience Match	30%
Semantic Similarity	10%
Baseline / Education	20%

⚠️ No black-box deep learning is used for final decision-making.
The system prioritizes interpretability and robustness, similar to real hiring systems.

🧠 NLP & ML Concepts Used

Resume document parsing

Regular Expressions for structured data extraction

Natural Language Processing (SpaCy)

Skill keyword matching

TF-IDF Vectorization

Cosine Similarity

Explainable rule-based scoring systems

🖥️ How to Run Locally
1️⃣ Clone the repository
git clone https://github.com/your-username/ATS-Resume-Intelligence.git
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

Goes beyond resume parsing by implementing ATS-style ranking

Fully job-specific, not a generic score

End-to-end system (backend + frontend + deployment)

Focuses on explainability, not black-box ML

Highly relevant to HR tech, AI, and real-world ML systems

🔮 Future Enhancements

Skill synonym normalization using embeddings

Education & degree relevance scoring

Configurable ATS weight sliders

Resume improvement suggestions

Multi-resume ranking

👤 Author

Atharva Rahate
B.Tech – Computer Technology
Interest Areas: AI, Machine Learning, NLP