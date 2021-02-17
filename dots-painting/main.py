import turtle as turtle_module
import random

turtle_module.colormode(255)
vilka = turtle_module.Turtle()
vilka.speed("fastest")
vilka.penup()
vilka.hideturtle()
color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]
vilka.setheading(225)
vilka.forward(300)
vilka.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    vilka.dot(20, random.choice(color_list))
    vilka.forward(50)

    if dot_count % 10 == 0:
        vilka.setheading(90)
        vilka.forward(50)
        vilka.setheading(180)
        vilka.forward(500)
        vilka.setheading(0)




screen = turtle_module.Screen()
screen.exitonclick()