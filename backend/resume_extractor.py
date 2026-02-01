import pdfplumber
import docx
import os

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


if __name__ == "__main__":
    path = input("Enter resume path: ")
    print(text_extract(path))