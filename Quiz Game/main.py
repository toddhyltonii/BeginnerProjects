from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for new_question in question_data:
    question_bank.append(
        Question(new_question["question"], new_question["correct_answer"])
    )

quiz = QuizBrain(question_bank)

while quiz.still_has_questions() == True:
    quiz.next_question()

print("You have completed the quiz!")
print(f"Your final score was: {quiz.score}/{quiz.q_number}")
