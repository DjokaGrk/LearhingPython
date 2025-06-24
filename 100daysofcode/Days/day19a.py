from turtle import Turtle, Screen
import random

ekran = Screen()
ekran.setup(width=700, height=500)
user_bet = ekran.textinput(
    title="Make your bet",
    prompt="who will win the race: black, blue, yellow, green, or red?",
)
print(user_bet)
# Define turtle colors, and y-positions
turtle_specs = [
    ("black", 0),
    ("blue", -30),
    ("yellow", -60),
    ("green", -90),
    ("red", -120),
]
is_race_on = False
turtles = {}
start_x = -330  # Far left position
for color, y in turtle_specs:
    t = Turtle()
    t.shape("turtle")
    t.color(color)
    t.penup()
    t.goto(start_x, y)
    turtles[color] = (
        t  # Optional: store turtles by name if you need to reference them later)
    )
if user_bet:
    is_race_on = True
while is_race_on:
    for color, turtle in turtles.items():
        if turtle.xcor() > 330:
            is_race_on = False
            if color == user_bet:
                print(f"You win! {color} is the winner!")
            else:
                print(f"You lose! {color} is the winner!")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


ekran.exitonclick()
