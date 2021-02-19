from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")

#creating a snake body from 3 squares
original_x = 0
original_y = 0
next_x = original_x -20

for t in range(4):
    new_snake = Turtle(shape="square")
    new_snake.color("white")
    new_snake.setx(original_x)
    new_snake.sety(original_y)
    original_x = next_x

























screen.exitonclick()