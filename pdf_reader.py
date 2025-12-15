# module for data processing and verification
from dataset import question, answers

def process_data():
    """
    Processes and verifies the dataset questions and answers.
    """
    print(f"Total Questions: {len(question)}")
    print(f"Total Answers: {len(answers)}")
    
    train_dataset = []
    for i in range(len(question)):
        q = question[i]
        a = answers[i].replace('\n', '')
        train_dataset.append([q, a])

    print(f"Processed {len(train_dataset)} items.")
    if len(train_dataset) > 0:
        print("Sample item:")
        print(train_dataset[0])

if __name__ == "__main__":
    process_data()