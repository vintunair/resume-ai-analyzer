import PyPDF2
from typing import IO


def extract_text_from_pdf(file_path: str) -> str:
    """
    Extract text from a PDF stored on disk.
    """
    text = ""
    with open(file_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text() + "\n"
    return text


def extract_text_from_pdf_file(file_obj: IO[bytes]) -> str:
    """
    Extract text from a PDF file-like object (e.g. Streamlit upload).
    """
    text = ""
    reader = PyPDF2.PdfReader(file_obj)
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text

