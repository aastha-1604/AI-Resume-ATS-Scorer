from pathlib import Path

from pypdf import PdfReader
from docx import Document


# ---------------------------------------------------------
# EXTRACT TEXT FROM PDF
# ---------------------------------------------------------

def extract_pdf_text(file_path: str) -> str:
    """
    Extract text from a PDF resume.
    """

    reader = PdfReader(file_path)

    text = ""

    for page in reader.pages:

        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text.strip()


# ---------------------------------------------------------
# EXTRACT TEXT FROM DOCX
# ---------------------------------------------------------

def extract_docx_text(file_path: str) -> str:
    """
    Extract text from a DOCX resume.
    """

    document = Document(file_path)

    paragraphs = []

    for paragraph in document.paragraphs:

        if paragraph.text.strip():
            paragraphs.append(paragraph.text)

    return "\n".join(paragraphs)


# ---------------------------------------------------------
# DETECT FILE TYPE AND EXTRACT TEXT
# ---------------------------------------------------------

def extract_resume_text(file_path: str) -> str:
    """
    Detect whether file is PDF or DOCX and extract text.
    """

    file_extension = Path(file_path).suffix.lower()

    if file_extension == ".pdf":

        return extract_pdf_text(file_path)

    elif file_extension == ".docx":

        return extract_docx_text(file_path)

    else:

        raise ValueError(
            "Unsupported file format. Please upload PDF or DOCX."
        )


# ---------------------------------------------------------
# TEST CODE
# ---------------------------------------------------------

if __name__ == "__main__":

    # Change this filename according to your actual file
    resume_path = "data/Aastha-Tech-Resume.pdf"

    try:

        extracted_text = extract_resume_text(
            resume_path
        )

        print("\n==============================")
        print("EXTRACTED RESUME TEXT")
        print("==============================\n")

        print(extracted_text)

    except Exception as e:

        print("Error:", e)