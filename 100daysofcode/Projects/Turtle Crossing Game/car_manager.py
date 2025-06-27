from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
x = 300

class CarManager:
  def __init__(self):
    self.all_cars = []
    self.car_speed = STARTING_MOVE_DISTANCE


  def create_car(self):
    random_chance = random.randint(1, 6)
    if random_chance == 1: # create car when is random_chance get 1
      new_car = Turtle("square") #shape add here aswell
      new_car.shapesize(stretch_wid=1, stretch_len=2)
      new_car.penup()
      new_car.color(random.choice(COLORS))
      y = random.randint(-250, 250)
      new_car.goto(x, y)
      self.all_cars.append(new_car) # append new_car to all_cars
  def move_cars(self):
    for car in self.all_cars:
      car.backward(self.car_speed)
  def level_up(self):
    self.car_speed += MOVE_INCREMENT

