"""
Verify the integrity of the dataset in dataset.py.

Checks that:
- question and answers lists have the same length
- no entries are empty
- prints a summary and sample item
"""
from dataset import question, answers


def verify():
    print(f"Total questions: {len(question)}")
    print(f"Total answers:   {len(answers)}")

    if len(question) != len(answers):
        print(f"ERROR: length mismatch ({len(question)} questions vs {len(answers)} answers)")
        return False

    empty_questions = [i for i, q in enumerate(question) if not q.strip()]
    empty_answers = [i for i, a in enumerate(answers) if not a.strip()]

    if empty_questions:
        print(f"WARNING: empty questions at indices {empty_questions}")
    if empty_answers:
        print(f"WARNING: empty answers at indices {empty_answers}")

    if not empty_questions and not empty_answers:
        print("All entries are non-empty.")

    print(f"\nSample (index 0):")
    print(f"  Q: {question[0]}")
    answer_preview = answers[0].replace('\n', ' ').strip()[:200]
    print(f"  A: {answer_preview}...")

    return True


if __name__ == "__main__":
    ok = verify()
    if ok:
        print("\nDataset verification passed.")
    else:
        print("\nDataset verification FAILED.")
