from question_model import Question
from data import question_data

question_bank = []
for item in question_data:
    q_text = item["text"]
    q_answer = item["answer"]
    question = Question(q_text, q_answer)
    question_bank.append(question)

print(question_bank)




