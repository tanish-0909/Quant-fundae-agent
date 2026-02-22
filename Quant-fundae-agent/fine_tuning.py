import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from dataset import question, answers

load_dotenv()


def main():
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        print("Error: GOOGLE_API_KEY environment variable not found.")
        sys.exit(1)

    client = genai.Client(api_key=api_key)

    print(f"Loaded {len(question)} questions and {len(answers)} answers.")

    # Build training examples from the dataset
    training_examples = [
        types.TuningExample(
            text_input=q,
            output=a.replace('\n', ''),
        )
        for q, a in zip(question, answers)
    ]

    training_dataset = types.TuningDataset(examples=training_examples)

    print(f"Prepared {len(training_examples)} training examples.")
    print("Starting tuning job...")

    try:
        tuning_job = client.tunings.tune(
            base_model='models/gemini-1.5-flash-001-tuning',
            training_dataset=training_dataset,
            config=types.CreateTuningJobConfig(
                epoch_count=6,
                batch_size=4,
                learning_rate=0.001,
                tuned_model_display_name="quant tuned model 1"
            )
        )
        print(f"Tuning job started: {tuning_job.name}")
        print(
            "Tuning takes time. Check Google AI Studio for job status.\n"
            "Once complete, set the TUNED_MODEL_NAME environment variable\n"
            "to the tuned model name, then run starter.py to use it."
        )

    except Exception as e:
        print(f"An error occurred during tuning: {e}")


if __name__ == "__main__":
    main()