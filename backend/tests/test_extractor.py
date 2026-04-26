import os
from backend.extractor import process_pdf
from pathlib import Path

# Testing purposes only
EXPECTED_DATA = {
    "16_infographic_lending.pdf": "called payday advances",
    "OIC-144-Payday-Loans-Regulation.pdf": "$300 for 14 days",
    "20484_payday_appendix_1_e.pdf": "Payday Loans Regulation"
}


def validation_check():
    BASE_DIR = Path(__file__).resolve().parent.parent
    SAMPLE_DOCS_DIR = BASE_DIR / "tests" / "sample_docs"
    pdf_files = list(SAMPLE_DOCS_DIR.glob("*.pdf"))

    print(f"VALIDATION CHECK: {len(pdf_files)} FILES\n")

    for pdf_file in pdf_files:
        print(f"FILE: {pdf_file.name}")
        print()
        text = process_pdf(pdf_file.name)

        if not text:
            print("EMPTY STRING\n")
            continue

        # Print the first 500 chars for manual review
        print("HEAD (First 500 Chars)")
        print(text[:500].replace('\n', ' \\n '))  # Show line breaks explicitly
        print("-------------------------------------------------------------")
        print()

        # Check for keywords
        expected = EXPECTED_DATA.get(pdf_file.name, "loan")
        if expected.lower() in text.lower():
            print(f"  VALIDATION: Found expected string '{expected}'")
        else:
            print(f"  VALIDATION: Missing '{expected}' - Extraction may be garbled.")

        # Checking for common OCR noise
        noise_chars = ['|', '!', '°', '©', '®']
        noise_count = sum(text.count(c) for c in noise_chars)
        if noise_count > 50:
            print(f"   WARNING: High noise detected ({noise_count} special chars).")

        print("\n" + "=" * 50 + "\n")


if __name__ == "__main__":
    validation_check()