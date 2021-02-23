from turtle import Screen, Turtle
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)



segments=[]

for position in starting_positions:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)
screen.update()


game_on = True

while game_on:

    screen.update()
    time.sleep(0.1)

    for block_number in range(len(segments)-1, 0, -1):
        moved_x = segments[block_number-1].xcor()
        moved_y = segments[block_number-1].ycor()
        segments[block_number].goto(moved_x, moved_y)
    segments[0].forward(20)
    segments[0].left(90)
























screen.exitonclick()