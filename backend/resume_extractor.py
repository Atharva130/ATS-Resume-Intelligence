import pdfplumber
import docx
import os
import re
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


nlp = spacy.load("en_core_web_sm")

SKILL_SET = {
    "python", "java", "c", "c++", "javascript",
    "machine learning", "deep learning", "nlp",
    "data science", "flask", "django",
    "sql", "mysql", "postgresql",
    "tensorflow", "pytorch",
    "html", "css", "react", "node"
}

def semantic_similarity(resume_text, jd_text):
    vectorizer = TfidfVectorizer(stop_words="english")
    vectors = vectorizer.fit_transform([resume_text, jd_text])

    similarity = cosine_similarity(
        vectors[0:1],  
        vectors[1:2]   
    )

    return similarity[0][0]


def extract_skills(text):
    doc = nlp(text.lower())
    found_skills = set()

    for token in doc:
        if token.text in SKILL_SET:
            found_skills.add(token.text)

    for chunk in doc.noun_chunks:
        if chunk.text in SKILL_SET:
            found_skills.add(chunk.text)

    return list(found_skills)


def text_extract(fpath):
    if not os.path.exists(fpath):
        raise FileNotFoundError("File does not exist.")
    _, ext = os.path.splitext(fpath)
    ext = ext.lower()
    if ext == ".pdf":
        return pdf_text(fpath)
    elif ext == ".docx":
        return docx_text(fpath)
    else:
        raise ValueError("Unsupported File Format.")

def pdf_text(fpath):
    text=""
    with pdfplumber.open(fpath) as pdf:
        for page in pdf.pages:
            pagetext = page.extract_text()
            if pagetext:
                text+=pagetext + "\n"
    return text

def docx_text(fpath):
    doc = docx.Document(fpath)
    text =[]
    for para in doc.paragraphs:
        if para.text.strip():
            text.append(para.text)
    return "\n".join(text)

def extract_email(text):
    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    match = re.search(pattern, text)
    return match.group() if match else None

def extract_phone(text):
    pattern = r"(\+?\d[\d\s\-()]{8,}\d)"
    match = re.search(pattern, text)
    return match.group() if match else None

def extract_experience(text):
    pattern = r"(\d+)\+?\s*(years|year|yrs|yr)\s*(of)?\s*(experience)?"
    matches = re.findall(pattern, text.lower())
    if matches:
        years = [int(match[0]) for match in matches]
        return max(years)
    return None

def process_job_description(jd_text):
    jd_skills = extract_skills(jd_text)
    jd_experience = extract_experience(jd_text)
    return jd_skills, jd_experience

def skill_match_score(resume_skills, jd_skills):
    if not jd_skills:
        return 0
    matched = set(resume_skills) & set(jd_skills)
    return len(matched) / len(jd_skills)

def experience_score(resume_exp, jd_exp):
    if jd_exp is None or resume_exp is None:
        return 0.5
    if resume_exp >= jd_exp:
        return 1.0
    return resume_exp / jd_exp

def ats_score(resume_text, jd_text):
    resume_skills = extract_skills(resume_text)
    resume_exp = extract_experience(resume_text)

    jd_skills, jd_exp = process_job_description(jd_text)

    skill_score = skill_match_score(resume_skills, jd_skills)
    exp_score = experience_score(resume_exp, jd_exp)
    semantic_score = semantic_similarity(resume_text, jd_text)

    final_score = (
        0.4 * skill_score +
        0.3 * exp_score +
        0.1 * semantic_score +
        0.2
    )

    return round(final_score * 100, 2)


if __name__ == "__main__":
    path = input("Enter resume path: ")
    text = text_extract(path)

    print("Email:", extract_email(text))
    print("Phone:", extract_phone(text))
    print("Experience (years):", extract_experience(text))
    print("Skills:", extract_skills(text))
    jd = input("Paste Job Description: ")
    score = ats_score(text, jd)
    print("ATS Score:", score)
