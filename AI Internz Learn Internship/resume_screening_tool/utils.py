from pdfminer.high_level import extract_text as pdf_extract_text
from docx import Document
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def extract_text(file_path):
    """
    Extract text from a resume or job description based on file type (PDF or DOCX).
    """
    if file_path.endswith(".pdf"):
        return pdf_extract_text(file_path)
    elif file_path.endswith(".docx"):
        doc = Document(file_path)
        return "\n".join([para.text for para in doc.paragraphs])
    else:
        with open(file_path, 'r') as file:
            return file.read()

def calculate_similarity(resume_text, job_desc_text):
    """
    Calculate similarity between resume and job description using Cosine Similarity.
    """
    documents = [resume_text, job_desc_text]
    
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(documents)
    
    return cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()[0]
