from turtle import Screen, Turtle
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

#creating a snake body from 3 squares

#i created my turtle using a for loop where there are original coordinates and then the next turtle will be added to the
#tail of the previous one


original_x = 0
original_y = 0
snake_blocks=[]

for t in range(3):
    next_x = original_x - 20
    new_snake = Turtle(shape="square")
    new_snake.penup()
    new_snake.color("white")
    new_snake.setx(original_x)
    new_snake.sety(original_y)
    original_x = next_x
    snake_blocks.append(new_snake)
screen.update()


game_on = True

while game_on:

    screen.update()
    time.sleep(0.1)

    for block_number in range(len(snake_blocks)-1, 0, -1):
        moved_x = snake_blocks[block_number-1].xcor()
        moved_y = snake_blocks[block_number-1].ycor()
        snake_blocks[block_number].goto(moved_x, moved_y)
    snake_blocks[0].forward(20)
    snake_blocks[0].left(90)
























screen.exitonclick()