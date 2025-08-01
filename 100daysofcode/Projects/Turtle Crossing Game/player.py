from turtle import Turtle as T
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(T):
    def __init__(self):
      super().__init__()
      self.shape("turtle")
      self.penup()
      self.go_to_start()
      self.setheading(90)

    def move(self):
      self.forward(MOVE_DISTANCE)
      self.speed("fastest")

    def go_to_start(self):
      self.goto(STARTING_POSITION)

    def is_cross_line(self):
      if self.ycor() > FINISH_LINE_Y:
        return True
      else:
        return False
