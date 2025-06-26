from turtle import Turtle

POSITION = [(350, 0), (-350, 0)]  # Right and left paddle positions
MOVE_DISTANCE = 20
UP = 90
DOWN = 270


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()  # Initialize the Turtle class
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    def move_up(self):
        self.new_y = self.ycor() + MOVE_DISTANCE
        self.speed("fastest")
        # Prevent paddle from moving out of bounds
        if self.new_y < 280:  # Prevent paddle from moving out of bounds
            self.sety(self.new_y)

    def move_down(self):
        self.new_y = self.ycor() - MOVE_DISTANCE
        self.speed("fastest")
        # Prevent paddle from moving out of bounds
        if self.new_y > -280:  # Prevent paddle from moving out of bounds
            self.sety(self.new_y)
