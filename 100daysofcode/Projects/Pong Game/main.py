from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time

# Set up the screen
s = Screen()
s.tracer(0)  # Turn off the screen updates for better performance
right_paddle = Paddle((350, 0))  # Right paddle
left_paddle = Paddle((-350, 0))  # Left paddle
ball = Ball()  # Create a ball instance

# Set the initial position and direction of the ball
ball.reset_position()
# Screen setup
s.setup(width=800, height=600)
s.bgcolor("black")
s.title("Pong Game by DjokaGrk")
# Listen for key presses = move paddles
s.listen()
s.onkey(right_paddle.move_up, "Up")
s.onkey(right_paddle.move_down, "Down")
s.onkey(left_paddle.move_up, "w")
s.onkey(left_paddle.move_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)  # Control the speed of the ball
    s.update()
    ball.move()

    # Detect collision with top and bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # Detect collision with paddles
    elif (ball.distance(right_paddle) < 50 and ball.xcor() > 320) or (
        ball.distance(left_paddle) < 50 and ball.xcor() < -320
    ):
        ball.bounce_x()
    elif ball.xcor() > 380 or ball.xcor() < -380:
        ball.reset_position()
