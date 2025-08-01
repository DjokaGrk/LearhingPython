class QuizBrain:
    """
    Manages the quiz logic, tracks questions, user score, and handles user interaction.
    """

    def __init__(self, q_list):
        """
        Initialize the QuizBrain with a list of Question objects.
        """
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        """
        Returns True if there are more questions to ask.
        """
        return self.question_number < len(self.question_list)

    def next_question(self):
        """
        Presents the next question to the user and checks the answer.
        """
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(
            f"Q.{self.question_number}: {current_question.text} (True or False): "
        )
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        """
        Checks the user's answer against the correct answer and updates the score.
        """
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("You are wrong. ")
        print(f"The correct answer is: {correct_answer}")
        print(f"Your corrent score is: {self.score}/{self.question_number}")
        print("\n")
