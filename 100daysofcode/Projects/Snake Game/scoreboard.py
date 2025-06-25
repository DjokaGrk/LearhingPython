from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.goto(0, 270)
        self.score = 0
        self.high_score = 0
        self.load_high_score()
        self.penup()
        self.hideturtle()
        self.write("Score: 0", align="center", font=("Arial", 18, "normal"))
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(
            f"Score: {self.score} High Score: {self.high_score}",
            align="center",
            font=("Arial", 18, "normal"),
        )

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()

    def load_high_score(self):
        try:
            with open("high_score.txt", "r") as file:
                self.high_score = int(file.read())
        except FileNotFoundError:
            self.high_score = 0

    def save_high_score(self):
        with open("high_score.txt", "w") as file:
            file.write(str(self.high_score))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
