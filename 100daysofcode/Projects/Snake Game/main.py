from turtle import Screen as S
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

s = S()
s.setup(width=600, height=600)
s.bgcolor("black")
s.title("Snake Game by DjokaGrk")
s.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()
s.listen()
# Listening to the key presses for moving the snake
s.onkey(snake.up, "w")
s.onkey(snake.down, "s")
s.onkey(snake.left, "a")
s.onkey(snake.right, "d")
# Moving the segments
game_is_on = True
while game_is_on:
    s.update()
    time.sleep(0.1)
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()


s.exitonclick()
