from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.all_cars = []

    def creating_car(self):
        a_chance = random.randint(1, 6)
        if a_chance == 5:
            car = Turtle()
            car.penup()
            car.shape("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.color(random.choice(COLORS))
            car.y_appear = random.randint(-250, 250)
            car.original_x = 300
            car.goto(car.original_x, car.y_appear)
            self.all_cars.append(car)


    def keep_moving(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)




