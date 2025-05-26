# importing required modules
from pypdf import PdfReader
from dataset import question, answers

print(len(question), len(answers))
train_dataset = []
for i in range(len(question)):
    q = question[i].replace('ﬁ', 'fi')
    a = answers[i].replace('\n', '').replace('f i', 'fi')
    train_dataset.append([q, a])

train_dataset2 = train_dataset
print(len(train_dataset))
print(train_dataset[0])