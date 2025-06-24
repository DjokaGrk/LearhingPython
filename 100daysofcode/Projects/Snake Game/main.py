from turtle import Screen as S
from snake import Snake
import time

s = S()
s.setup(width=600, height=600)
s.bgcolor("black")
s.title("Snake Game by DjokaGrk")
s.tracer(0)

snake = Snake()
s.listen()
s.onkey(snake.up, "Up")
s.onkey(snake.down, "Down")
s.onkey(snake.left, "Left")
s.onkey(snake.right, "Right")
s.onkey(snake.up, "w")
s.onkey(snake.down, "s")
s.onkey(snake.left, "a")
s.onkey(snake.right, "d")
# Moving the segmets
game_is_on = True
while game_is_on:
    s.update()
    time.sleep(0.1)
    snake.move()


s.exitonclick()
