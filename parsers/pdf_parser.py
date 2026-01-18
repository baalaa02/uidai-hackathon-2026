import pdfplumber
from io import BytesIO

def parse_pdf(binary_data):
    text = ""
    with pdfplumber.open(BytesIO(binary_data)) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text
