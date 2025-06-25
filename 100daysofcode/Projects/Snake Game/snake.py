from turtle import Turtle as T
import time

START_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]  # The first segment is the head of the snake

    def create_snake(self):
        for pos in START_POSITIONS:
            self.add_segment(pos)

    def add_segment(self, pos):
        segment = T("square")
        segment.color("white")
        segment.penup()
        segment.goto(pos)
        self.segments.append(segment)

    def extend(self):
        # Add a new segment to the snake
        self.add_segment(self.segments[-1].position())
        # Move the new segment to the position of the last segment
        # last_segment = self.segments[-2]
        # self.segments[-1].goto(last_segment.xcor(), last_segment.ycor())

    def reset(self):
        for segment in self.segments:
            segment.goto(1000, 1000)  # Move off-screen
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            # Segmets are moving last segment 1st and 2nd last then 1st
            # so thay can move all together
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
