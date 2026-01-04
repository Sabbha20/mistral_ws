import os
import fitz
import docx

def extract_text_from_pdf(file_path):
    """Extract text from a PDF file."""
    text = ""
    try:
        with fitz.open(file_path) as doc:
            for page in doc:
                text += page.get_text() + "\n"
    except Exception as e:
        print(f"Error reading PDF file {file_path}: {e}")
    return text

def extract_text_from_docx(file_path):
    """Extract text from a DOCX file."""
    text = ""
    try:
        doc = docx.Document(file_path)
        for para in doc.paragraphs:
            text += para.text + "\n"
    except Exception as e:
        print(f"Error reading DOCX file {file_path}: {e}")
    return text

def extract_text_from_txt(file_path):
    """Extract text from a TXT file."""
    text = ""
    try:
        with open(file_path, "r", encoding="utf-8") as txt:
            text = txt.read()
    except Exception as e:
        print(f"Error reading TXT file {file_path}: {e}")
    return text


def extract_text(file_path):
    """Load a document and extract its text based on file type."""
    _, file_extension = os.path.splitext(file_path)
    file_extension = file_extension.lower()

    if file_extension == ".pdf":
        return extract_text_from_pdf(file_path)
    elif file_extension == ".docx":
        return extract_text_from_docx(file_path)
    elif file_extension == ".txt":
        return extract_text_from_txt(file_path)
    else:
        print(f"Unsupported file type: {file_extension}")
        return ""
    
if __name__ == "__main__":
    resume_pdf = "./resume.pdf"
    resume_docx = "./resume.docx"
    resume_txt = "./resume.txt"
    
    print(extract_text(resume_pdf))