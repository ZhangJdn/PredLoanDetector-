import pytesseract
import pdfplumber
from pathlib import Path
from pdf2image import convert_from_path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
POPPLER_PATH = r'C:\Program Files\poppler-25.12.0\Library\bin'

BASE_DIR = Path(__file__).resolve().parent
SAMPLE_DOCS_DIR = BASE_DIR / "tests" / "sample_docs"

def process_pdf(filename):
    pdf_path = SAMPLE_DOCS_DIR / filename

    if not pdf_path.exists():
        print(f"ERROR: Could not find {pdf_path}")
        return ""

    full_text = []

    with pdfplumber.open(pdf_path) as pdf:
        for i, page in enumerate(pdf.pages):
            page_text = page.extract_text()

            if not page_text or len(page_text.strip()) < 10:
                print(f"Page {i + 1} has no digital text, using OCR instead.")

                images = convert_from_path(
                    pdf_path,
                    first_page=i + 1,
                    last_page=i + 1,
                    poppler_path=POPPLER_PATH
                )
                ocr_text = pytesseract.image_to_string(images[0])
                full_text.append(ocr_text)
            else:
                print(f"Page {i + 1} digital text extracted using pdf plumber.")
                full_text.append(page_text)
    return "".join(full_text)
