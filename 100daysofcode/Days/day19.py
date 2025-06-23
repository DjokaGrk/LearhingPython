from turtle import Turtle as T, Screen as S

alex = T()
ekran = S()


def move_forwards():
  alex.forward(10)

def move_backwards():
  alex.backward(10)

def turn_left():
  alex.left(10)

def turn_right():
  alex.right(10)

def clear_screen():
  alex.clear()
  alex.penup()
  alex.home()
  alex.pendown()

ekran.listen()
ekran.onkey(move_forwards, "w")
ekran.onkey(move_backwards, "s")
ekran.onkey(turn_left, "a")
ekran.onkey(turn_right, "d")
ekran.onkey(clear_screen, "c")
ekran.exitonclick()
