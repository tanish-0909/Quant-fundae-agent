import re
import os
from PyPDF2 import PdfReader


PDF_PATH = os.path.join(os.path.dirname(__file__), "FAQs in quant.pdf")
OUTPUT_PATH = os.path.join(os.path.dirname(__file__), "dataset.py")


def extract_text_from_pdf(pdf_path):
    """Read every page of the PDF and return the full text."""
    reader = PdfReader(pdf_path)
    full_text = ""
    for page in reader.pages:
        text = page.extract_text()
        if text:
            full_text += text + "\n"
    return full_text


def parse_questions_and_answers(text):
    """
    Split the extracted text into question/answer pairs.

    Each FAQ entry starts with a question line (ending with '?')
    followed by a 'Short answer' block and usually an 'Example' block.
    We split on lines that look like standalone questions.
    """
    # Pattern: a line that is mostly a question (ends with ?)
    # We look for lines that start a new FAQ entry.
    question_pattern = re.compile(
        r"^(.+\?)\s*$", re.MULTILINE
    )

    questions = []
    answers = []

    matches = list(question_pattern.finditer(text))

    for idx, match in enumerate(matches):
        q = match.group(1).strip()

        # answer runs from end of question to start of next question
        start = match.end()
        if idx + 1 < len(matches):
            end = matches[idx + 1].start()
        else:
            end = len(text)

        answer_text = text[start:end].strip()

        if answer_text:
            questions.append(q)
            answers.append(answer_text)

    return questions, answers


def write_dataset(questions, answers, output_path):
    """Write the extracted Q&A pairs to dataset.py as Python lists."""
    with open(output_path, "w", encoding="utf-8") as f:
        # write questions list
        f.write("question = [\n")
        for q in questions:
            escaped = q.replace("\\", "\\\\").replace('"', '\\"')
            f.write(f'    "{escaped}",\n')
        f.write("]\n\n")

        # write answers list
        f.write("answers = [\n")
        for a in answers:
            f.write('    """\n')
            for line in a.split("\n"):
                f.write(f"    {line}\n")
            f.write('    """,\n')
        f.write("]\n")


def main():
    if not os.path.exists(PDF_PATH):
        print(f"Error: PDF not found at {PDF_PATH}")
        return

    print(f"Reading PDF: {PDF_PATH}")
    text = extract_text_from_pdf(PDF_PATH)
    print(f"Extracted {len(text)} characters of text.")

    questions, answers = parse_questions_and_answers(text)
    print(f"Parsed {len(questions)} question-answer pairs.")

    write_dataset(questions, answers, OUTPUT_PATH)
    print(f"Dataset written to {OUTPUT_PATH}")

    if questions:
        print(f"\nSample question: {questions[0]}")
        print(f"Sample answer (first 200 chars): {answers[0][:200]}...")


if __name__ == "__main__":
    main()