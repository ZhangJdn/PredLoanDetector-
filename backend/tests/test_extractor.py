from backend.extractor import process_pdf
from backend.tests import sample_docs
from pathlib import Path

def run_suite():
    test_files = [
        {"name": "digital_test.pdf", "expected_method": "digital"},
        {"name": "scanned_test.pdf", "expected_method": "ocr"}
    ]

    for test in test_files:
        print(f"\n>>> TESTING: {test['name']}")
        try:
            # 2. Run your processing logic
            content = process_pdf(test['name'])

            # 3. Basic Validation
            if content and len(content) > 100:
                print(f"SUCCESS: Extracted {len(content)} characters.")

                # Check for a keyword you know is in the doc
                if "Interest" in content or "Loan" in content:
                    print("VERIFIED: Core keywords found.")
            else:
                print("WARNING: Extraction returned very little text.")

        except Exception as e:
            print(f"FAILED: An error occurred: {e}")


if __name__ == "__main__":
    run_suite()