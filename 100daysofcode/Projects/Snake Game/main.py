from turtle import Screen as S, Turtle as T

s = S()
s.setup(width=600, height=600)
s.bgcolor("black")
s.title("Snake Game by DjokaGrk")

segments = []
start_positions = [(0, 0), (-20, 0), (-40, 0)]

for pos in start_positions:
    segment = T(shape="square")
    segment.color("white")
    segment.penup()
    segment.goto(pos)
    segments.append(segment)
s.exitonclick()
