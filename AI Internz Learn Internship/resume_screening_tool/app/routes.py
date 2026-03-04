from flask import render_template, request
from app import app
from utils import extract_text, calculate_similarity

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        resume = request.files['resume']
        job_desc = request.files['job_desc']
        
        # Save uploaded files
        resume_path = "data/resumes/resume.pdf"
        job_desc_path = "data/resumes/job_desc.txt"
        resume.save(resume_path)
        job_desc.save(job_desc_path)

        # Extract text and calculate similarity
        resume_text = extract_text(resume_path)
        job_desc_text = extract_text(job_desc_path)
        similarity = calculate_similarity(resume_text, job_desc_text)

        return render_template('index.html', similarity=similarity)

    return render_template('index.html')
