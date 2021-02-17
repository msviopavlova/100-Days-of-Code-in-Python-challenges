import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


tim.speed("fastest")
for _ in range(120):
    tim.circle(100)
    tim.pencolor(random_color())
    tim.circle(3, 3)



screen = Screen()
screen.exitonclick()
