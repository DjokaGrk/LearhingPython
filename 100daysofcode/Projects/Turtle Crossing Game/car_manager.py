from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 600  # Set to 600 for your screen


class CarManager:
    def __init__(self):
        self.cars = []  # Will store tuples: (car_turtle, move_distance)

    def create_car(self):
        car = Turtle("square")
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.color(random.choice(COLORS))
        car.penup()
        random_y = random.randint(-SCREEN_HEIGHT // 2 + 20, SCREEN_HEIGHT // 2 - 20)
        car.goto(SCREEN_WIDTH // 2, random_y)
        move_distance = STARTING_MOVE_DISTANCE  # Each car starts at 5 px/frame
        self.cars.append((car, move_distance))

    def move_cars(self):
        for car, move_distance in self.cars:
            car.backward(move_distance)

    def level_up(self):
        for i in range(len(self.cars)):
            car, move_distance = self.cars[i]
            self.cars[i] = (car, move_distance + MOVE_INCREMENT)
