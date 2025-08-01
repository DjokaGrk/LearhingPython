"""
Main script to run the quiz game.
Imports question data, creates question objects, and manages the quiz flow.
"""

from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    q_text = question["question"]
    q_answer = question["correct_answer"]
    new_question = Question(q_text, q_answer)
    question_bank.append(new_question)
quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
print("You've complated quiz your final score")
print(f"You final score is {quiz.score}/{quiz.question_number}")
