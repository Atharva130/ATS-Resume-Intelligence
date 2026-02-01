from flask import Flask, request, jsonify
from flask_cors import CORS

from resume_extractor import (
    text_extract,
    extract_email,
    extract_phone,
    extract_experience,
    extract_skills,
    ats_score
)

app = Flask(__name__)
CORS(app)

@app.route("/analyze", methods=["POST"])
def analyze_resume():
    resume_file = request.files.get("resume")
    jd_text = request.form.get("job_description")

    if not resume_file or not jd_text:
        return jsonify({"error": "Resume file and JD required"}), 400

    resume_path = f"temp_{resume_file.filename}"
    resume_file.save(resume_path)

    resume_text = text_extract(resume_path)

    result = {
        "email": extract_email(resume_text),
        "phone": extract_phone(resume_text),
        "experience": extract_experience(resume_text),
        "skills": extract_skills(resume_text),
        "ats_score": ats_score(resume_text, jd_text)
    }

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
