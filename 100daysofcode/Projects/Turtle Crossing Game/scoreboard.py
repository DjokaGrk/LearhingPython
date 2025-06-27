from turtle import Turtle, Screen

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 0
        self.hideturtle()  # Hide the turtle icon
        self.penup()
        self.color("black")
        self.goto(-80, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.level += 1
        self.write(f"level: {self.level}", font=FONT)

    def game_over(self):
        self.clear()  # This hides the previous scoreboard
        self.goto(-60, 0)
        self.write("Game Over", font=FONT)
        # Show the level below "Game Over"
        self.goto(-100, -40)
        self.write(f"Your  are level: {self.level}", font=FONT)
