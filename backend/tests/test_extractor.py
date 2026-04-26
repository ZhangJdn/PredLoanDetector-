import re
from backend.extractor import process_pdf
from pathlib import Path

# Testing purposes only. It validates that a certain phrase is in the
# pdf text so we know that it is working correctly
EXPECTED_DATA = {
    "16_infographic_lending.pdf": "cost of loan",
    "OIC-144-Payday-Loans-Regulation.pdf": "$300 for 14 days",
    "20484_payday_appendix_1_e.pdf": "Payday Loans Regulation"
}

def validate_financial_integrity(text):
    """
    Checks if dollar amounts ($14, $100) survived the extraction.
    """
    money_pattern = r"\$\s?\d+"
    matches = re.findall(money_pattern, text)
    return (True, len(matches), matches[:3]) if matches else (False, 0, [])

def validation_check():

    HIGH_NOISE_THRESHOLD = 50
    DIVIDER_MULTIPLIER = 50

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
        print("First 500 Chars for validation")
        print(text[:500].replace('\n', ' \\n '))
        print("-------------------------------------------------------------")
        print()

        is_valid, count, samples = validate_financial_integrity(text)

        if is_valid:
            print(f"  FINANCIAL DATA: Found {count} dollar amounts. Samples: {samples}")
        else:
            print("  FINANCIAL DATA: WARNING! No dollar amounts found.")

        # Check for keywords
        expected = EXPECTED_DATA.get(pdf_file.name, "loan")
        if expected.lower() in text.lower():
            print(f"  VALIDATION: Found expected string '{expected}'")
        else:
            print(f"  VALIDATION: Missing '{expected}' - Extraction may be garbled.")

        # Checking for common OCR noise
        noise_chars = ['|', '!', '@', '?', '#', '$', '%', '^', '&', '*']
        noise_count = sum(text.count(c) for c in noise_chars)
        # Measure how much noise in the data
        if noise_count > HIGH_NOISE_THRESHOLD:
            print(f"   WARNING: High noise detected ({noise_count} special chars).")

        print("\n" + "=" * DIVIDER_MULTIPLIER + "\n")


if __name__ == "__main__":
    validation_check()