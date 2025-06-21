from turtle import Turtle, Screen

pablo = Turtle()
pablo.shape("turtle")
pablo.color("seagreen")

for _ in range(4):
    pablo.forward(100)
    pablo.right(90)


screen = Screen()
screen.exitonclick()
