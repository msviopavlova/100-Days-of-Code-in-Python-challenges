from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(random.choice(COLORS))
        self.y_appear = range(-250, 250)
        self.original_x = 200
        self.goto(self.original_x, random.choice(self.y_appear))
       # self.keep_moving()

   # def keep_moving(self):
      #  for x in self.original_x:
      #      x -= STARTING_MOVE_DISTANCE
      #      self.goto(x, None)


