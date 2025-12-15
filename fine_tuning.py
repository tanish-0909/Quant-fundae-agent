import os
import sys
import time
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
    
    train_dataset = []
    for i in range(len(question)):
        q = question[i]
        a = answers[i].replace('\n', '')
        train_dataset.append([q, a])

    print(f"Prepared {len(train_dataset)} training examples.")
    # print(train_dataset[0])

    # for model_info in client.models.list():
    #     print(model_info.name)

    training_examples = [
        types.TuningExample(
            text_input=i,
            output=o,
        )
        for i, o in train_dataset
    ]

    training_dataset = types.TuningDataset(examples=training_examples)

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
        print("Model tuning takes time. Please wait for the job to complete in the Google AI Studio console before using the model.")
        
        # Note: Immediate inference is not possible until tuning is complete.
        
        """
        print("\nEnter a question to test (Note: Model might not be ready yet):")
        user_question = input()
        
        # generate content with the tuned model
        response = client.models.generate_content(
            model=tuning_job.tuned_model.model,
            contents=user_question,
        )
        print(response.text)
        """
        
    except Exception as e:
        print(f"An error occurred during tuning: {e}")

if __name__ == "__main__":
    main()