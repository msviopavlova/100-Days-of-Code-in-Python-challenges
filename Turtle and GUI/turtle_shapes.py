from turtle import Turtle, Screen
import random

lappi = Turtle()
lappi.shape("turtle")

#each time the sides increase my 1 corner
# 360/corner = the degrees of right turn
# start from triangle
# forward100 each time

random_color = ["forest green", "red", "cyan", "deep pink", "magenta", "purple", "gold", "orchid", "yellow", "blue"]
corner = 3
keep_drawing = True
while keep_drawing:
    lappi.pensize(5)
    for _ in range(corner): # because 6 shapes
        degrees = 360/corner
        lappi.right(degrees)
        lappi.forward(100)
    corner+=1
    lappi.pencolor(random.choice(random_color))

    if corner >=10:
         keep_drawing = False



screen = Screen()
screen.exitonclick()







