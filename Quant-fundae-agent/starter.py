import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

SYSTEM_PROMPT = (
    "You are an expert in quantitative finance. Answer questions about "
    "derivatives pricing, risk management, stochastic calculus, portfolio "
    "theory, and related topics. Be precise and use mathematical notation "
    "where appropriate. Provide both a short answer and an example when "
    "possible."
)


def main():
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        print("Error: GOOGLE_API_KEY environment variable not found.")
        sys.exit(1)

    client = genai.Client(api_key=api_key)

    # Use the fine-tuned model if available, otherwise fall back to base model
    tuned_model = os.getenv("TUNED_MODEL_NAME")
    model_name = tuned_model if tuned_model else "gemini-2.0-flash"

    if tuned_model:
        print(f"Using tuned model: {model_name}")
    else:
        print(f"No TUNED_MODEL_NAME set, using base model: {model_name}")

    prompt = input("Enter your query: ")

    try:
        config = types.GenerateContentConfig(
            max_output_tokens=2048,
            temperature=0.1
        )
        # Add system instruction only when using the base model
        if not tuned_model:
            config.system_instruction = SYSTEM_PROMPT

        response = client.models.generate_content(
            model=model_name,
            contents=[prompt],
            config=config,
        )
        print("\nResponse:")
        print(response.text)
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()