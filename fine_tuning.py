from google import genai
from google.genai import types
client = genai.Client(api_key="APIKEY") # Get the key from the GOOGLE_API_KEY env variable
from dataset import question, answers

print(len(question), len(answers))
train_dataset = []
for i in range(len(question)):
    q = question[i].replace('ﬁ', 'fi')
    a = answers[i].replace('\n', '').replace('f i', 'fi')
    train_dataset.append([q, a])

train_dataset2 = train_dataset

# for model_info in client.models.list():
#     print(model_info.name)

training_dataset=types.TuningDataset(
        examples=[
            types.TuningExample(
                text_input=i,
                output=o,
            )
            for i,o in train_dataset2
        ],
    )
tuning_job = client.tunings.tune(
    base_model='models/gemini-1.5-flash-001-tuning',
    training_dataset=training_dataset,
    config=types.CreateTuningJobConfig(
        epoch_count= 6,
        batch_size=4,
        learning_rate=0.001,
        tuned_model_display_name="quant tuned model 1"
    )
)

question = input()

# generate content with the tuned model
response = client.models.generate_content(
    model=tuning_job.tuned_model.model,
    contents=question,
)

print(response.text)