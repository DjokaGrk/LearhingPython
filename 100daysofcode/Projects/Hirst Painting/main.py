from turtle import Turtle as T, Screen as S
import random

color_list = [
    (202, 164, 110),
    (149, 75, 50),
    (222, 201, 136),
    (53, 93, 123),
    (170, 154, 41),
    (138, 31, 20),
    (134, 163, 184),
    (197, 92, 73),
    (47, 121, 86),
    (73, 43, 35),
    (145, 178, 149),
    (14, 98, 70),
    (232, 176, 165),
    (160, 142, 158),
    (54, 45, 50),
    (101, 75, 77),
    (183, 205, 171),
    (36, 60, 74),
    (19, 86, 89),
    (82, 148, 129),
    (147, 17, 19),
    (27, 68, 102),
    (12, 70, 64),
    (107, 127, 153),
    (176, 192, 208),
    (168, 99, 102),
]
alex = T()
screen = S()
alex.screen.colormode(255)
alex.speed("fastest")
alex.penup()
alex.hideturtle()
rows = 10
cols = 10
dot_size = 20
spacing = 50
start_x = -spacing * cols // 2
start_y = -spacing * rows // 2
# Draw grid
for row in range(rows):
    for col in range(cols):
        alex.goto(start_x + col * spacing, start_y + row * spacing)
        alex.dot(dot_size, random.choice(color_list))

# Keep window open
screen.exitonclick()
