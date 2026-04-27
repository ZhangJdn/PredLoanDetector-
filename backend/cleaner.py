import re

def clean_extracted_text(text):
    if not text:
        return ""

    text = re.sub(r'[_|]+', ' ', text)

    text = re.sub(r"(for|\d+)\s*\n\s*(\d+)", r"\1 \2", text)

    text = re.sub(r'\$\s+(\d)',r'$\1', text)
    text = re.sub(r'(\d)\s+%',r'\1%',text)

    text = re.sub(r'\s+', ' ', text).strip()
    return text

if __name__ == '__main__':
    sample = "The cost is a bit high. It is $ 300 for \n14 days."
    sample2 = "Annual Percentage Rate (APR) 14 %\nLoan Fee $ 15 per $100"
    print(f"Original: {sample2}")
    print(f"Cleaned:  {clean_extracted_text(sample2)}")