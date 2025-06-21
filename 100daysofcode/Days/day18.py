from turtle import Screen as S, Turtle as T

alex = T()
alex.shape("turtle")
alex.color("seagreen")

for _ in range(4):
    alex.forward(100)
    alex.right(90)


screen = S()
screen.exitonclick()
