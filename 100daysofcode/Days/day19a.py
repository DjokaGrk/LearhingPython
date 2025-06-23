from turtle import Turtle, Screen

ekran = Screen()
ekran.setup(width=900, height=400)
user_bet = ekran.textinput(
    title="Make your bet", prompt="who will win the race: alex,pablo,pera,trajko,rajko"
)
print(user_bet)
# Define turtle names, colors, and y-positions
turtle_specs = [
    ("alex", "black", 0),
    ("pablo", "blue", -30),
    ("pera", "yellow", -60),
    ("trajko", "green", -90),
    ("rajko", "red", -120),
]

turtles = {}
start_x = -450  # Far left position
for name, color, y in turtle_specs:
    t = Turtle()
    t.shape("turtle")
    t.color(color)
    t.penup()
    t.goto(start_x, y)
    turtles[name] = (
        t  # Optional: store turtles by name if you need to reference them later
    )

ekran.exitonclick()
