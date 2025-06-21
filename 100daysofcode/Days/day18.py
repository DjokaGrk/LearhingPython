from turtle import Turtle as t
import random

alex = t()
# alex.shape("turtle")
alex.speed("fastest")
alex.pensize(2)
# Set the color mode to 255 to use RGB values
alex.screen.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


# for _ in range(4):
#     alex.forward(100)
#     alex.right(90)
# for _ in range(20):
#   alex.pendown()
#   alex.forward(10)
#   alex.penup()
#   alex.forward(10)
# def draw_shape(sides, length=100):
#     angle = 360 / sides
#     for _ in range(sides):
#         alex.forward(length)
#         alex.right(angle)


# for sides in range(3, 11):
#     alex.color(random_color())
#     draw_shape(sides)


# directions = [0, 90, 180, 270]  # Possible directions (right angles)


# for _ in range(200):  # Number of steps in the random walk
#     alex.color(random_color())  # Optional: change color each step
#     alex.forward(30)  # Move forward
#     alex.setheading(random.choice(directions))  # Turn to a random direction
def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        alex.color(random_color())
        alex.circle(100)
        alex.setheading(alex.heading() + size_of_gap)


draw_spirograph(10)  # Change 10 for a different gap size
