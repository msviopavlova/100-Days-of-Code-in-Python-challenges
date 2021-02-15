from turtle import Turtle, Screen
import random

walker = Turtle()
walker.pensize(3)
random_color = ["forest green", "red", "cyan", "deep pink", "magenta", "purple", "gold", "orchid", "yellow", "blue"]

angles = [-270, -180, -90, 0,  90, 180, 270]
for move in range(100):
    walker.forward(15)
    random_right = random.choice(angles)
    walker.right(random_right)
    walker.pencolor(random.choice(random_color))





screen = Screen()
screen.exitonclick()




