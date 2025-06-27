from turtle import Turtle, Screen

FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 0
        self.hideturtle()  # Hide the turtle icon
        self.penup()
        self.color("black")
        self.goto(-280, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def game_over(self):
        self.clear()  # This hides the previous scoreboard
        self.goto(0, 0)
        self.write("Game Over", align="center", font=FONT)
        # Show the level below "Game Over"
        self.goto(0, -40)
        self.write(f"Your  are level: {self.level}", align="center", font=FONT)
