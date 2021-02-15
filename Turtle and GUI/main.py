from turtle import Turtle, Screen


lappi = Turtle()
lappi.shape("turtle")
lappi.color("red")




#each time the sides increase my 1 corner
# 360/corner = the degrees of right turn
# start from triangle
# forward100 each time


corner = 3
keep_drawing = True
while keep_drawing:

    for _ in range(corner): # because 6 shapes
        degrees = 360/corner
        lappi.right(degrees)
        lappi.forward(100)
    corner+=1

    if corner >=9:
         keep_drawing = False


screen = Screen()
screen.exitonclick()







