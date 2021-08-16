from question_model import Question
from data import question_data
from quiz_brain import QuizzBrain

data_bank = []

for row in question_data:
    data_bank.append(Question(row["question"], row["correct_answer"]))

brain = QuizzBrain(data_bank)

while brain.still_has_questions():
    brain.next_question()

print("You've completed the quiz!")
print(f"Your final score was: {brain.score}/{brain.question_number}")
