from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")  # Set the color of the scoreboard
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        # Write the scores at the top center of the screen
        self.goto(-100, 200)  # Position the scoreboard at the top center
        self.write(
            f"{self.left_score}",
            align="center",
            font=("Arial", 60, "normal"),
        )
        self.goto(0, 200)
        self.write(
            " : ",
            align="center",
            font=("Arial", 60, "normal"),
        )
        self.goto(100, 200)  # Position the scoreboard at the top center
        self.write(
            f"{self.right_score}",
            align="center",
            font=("Arial", 60, "normal"),
        )

    def increase_left_score(self):
        self.left_score += 1
        self.update_scoreboard()

    def increase_right_score(self):
        self.right_score += 1
        self.update_scoreboard()
