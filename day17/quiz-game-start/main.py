from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for q in question_data:
    question_text = q["text"]
    """question_text = q['question']"""# this is if you want to get questions from https://opentdb.com
    question_answer = q["answer"]
    """question_answer = q['correct_answer']"""# this is if you want to get questions from https://opentdb.com
    new_question = Question(q_text=question_text,q_answer=question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"your final score was: {quiz.score}/{quiz.question_number}" )