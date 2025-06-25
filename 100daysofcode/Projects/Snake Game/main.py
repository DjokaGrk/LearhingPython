from turtle import Screen as S
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

# Set up the screen
s = S()
s.setup(width=600, height=600)
s.bgcolor("black")
s.title("Snake Game by DjokaGrk")
s.tracer(0)

# Create game objects
snake = Snake()
food = Food()
scoreboard = ScoreBoard()

paused = False
game_is_on = True
quit_game = False  # Add this flag


def toggle_pause():
    global paused
    paused = not paused
    if paused:
        scoreboard.show_pause()
    else:
        scoreboard.clear_pause()


def restart_game():
    global game_is_on, paused
    snake.reset()
    scoreboard.reset()
    food.refresh()
    paused = False
    scoreboard.clear_pause()
    game_is_on = True


def quit_program():
    global quit_game
    quit_game = True


# Difficulty selection
DIFFICULTY_SPEEDS = {"normal": 0.13, "fast": 0.08, "fastest": 0.04}
DIFFICULTY_MAP = {"1": "normal", "2": "fast", "3": "fastest"}

difficulty_input = s.textinput(
    "Difficulty", "Choose difficulty:\n1 - normal\n2 - fast\n3 - fastest"
)
if difficulty_input and difficulty_input in DIFFICULTY_MAP:
    difficulty = DIFFICULTY_MAP[difficulty_input]
else:
    difficulty = "normal"
snake_speed = DIFFICULTY_SPEEDS[difficulty]

# Key bindings
s.listen()
s.onkey(toggle_pause, "p")
s.onkey(restart_game, "r")
s.onkey(quit_program, "q")  # Press 'q' to quit
s.onkey(snake.up, "w")
s.onkey(snake.down, "s")
s.onkey(snake.left, "a")
s.onkey(snake.right, "d")

while not quit_game:
    s.update()
    time.sleep(snake_speed)
    if game_is_on and not paused:
        snake.move()

        # Detect collision with food
        if snake.head.distance(food) < 15:
            food.refresh()
            scoreboard.increase_score()
            snake.extend()

        # Edge wrapping
        if snake.head.xcor() > 290:
            snake.head.setx(-290)
        elif snake.head.xcor() < -290:
            snake.head.setx(290)
        elif snake.head.ycor() > 290:
            snake.head.sety(-290)
        elif snake.head.ycor() < -290:
            snake.head.sety(290)

        # Detect collision with tail
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                scoreboard.game_over()
                scoreboard.reset()
                game_is_on = False
                break

s.bye()  # This will close the turtle graphics window
