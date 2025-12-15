# Quant Fundae Agent

This project implements an AI agent specialized in answering quantitative finance questions. It leverages the Google Gemini model.

## Features

- **Standard Query Engine**: A basic interface to query the Gemini model using the `starter.py` script.
- **Fine-Tuning Capability**: Scripts to fine-tune the Gemini model on a specialized dataset of quantitative finance questions (`fine_tuning.py`).
- **Data Processing**: Utilities to process and verify the training dataset (`pdf_reader.py`).

## File Structure

- `dataset.py`: Contains the raw dataset of questions and answers.
- `fine_tuning.py`: Script to initiate a fine-tuning job on the Gemini model.
- `pdf_reader.py`: Utility script to verify and process the dataset.
- `starter.py`: Main entry point for interacting with the base Gemini model.
- `requirements.txt`: Python dependencies.

## Setup and Installation

1.  **Clone the repository** to your local machine.

2.  **Install dependencies**:
    Ensure you have Python installed, then run:

    pip install -r requirements.txt

3.  **Environment Configuration**:
    Create a `.env` file in the root directory and add your Google API key:

    GOOGLE_API_KEY=your_api_key_here

## Usage

### Running the Basic Agent

To run the standard agent and ask questions:

python starter.py

You will be prompted to enter your query.

### Fine-Tuning the Model

To start a fine-tuning job with the provided dataset:

python fine_tuning.py

Note: This script initiates a tuning job on Google's servers. The job takes time to complete. Once finished, you can update the `starter.py` or a new script to use the specific `tuned_model` name associated with your project.

### Verifying Data

To check the integrity of the dataset:

python pdf_reader.py
