from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 18, "normal")


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
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(
            f"Score: {self.score} High Score: {self.high_score}",
            align=ALIGNMENT,
            font=FONT,
        )

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
        self.save_high_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score()
        self.score = 0
        self.update_scoreboard()

    def save_high_score(self):
        with open("high_score.txt", "w") as file:
            file.write(str(self.high_score))

    def load_high_score(self):
        try:
            with open("high_score.txt") as file:
                self.high_score = int(file.read())
        except FileNotFoundError:
            self.high_score = 0

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def show_pause(self):
        self.goto(0, 50)
        self.write("PAUSED", align=ALIGNMENT, font=("Arial", 24, "bold"))

    def clear_pause(self):
        self.clear()
        self.goto(0, 270)  # Move back to the top
        self.update_scoreboard()
