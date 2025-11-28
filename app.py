import json

from parser import extract_text_from_pdf
from rewrite_engine import analyze_resume


def main():
    pdf_path = "demo/sample_resume.pdf"

    print("Extracting resume text...")
    text = extract_text_from_pdf(pdf_path)

    print("Analyzing with AI...")
    insights = analyze_resume(text)

    print("Saving output...")
    with open("demo/output.json", "w") as f:
        json.dump(insights, f, indent=2)

    print("Done! Check demo/output.json")


if __name__ == "__main__":
    main()

