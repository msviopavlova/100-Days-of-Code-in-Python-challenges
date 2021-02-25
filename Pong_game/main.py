from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)




right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))

ball = Ball()
ball.go_to_coordinate((350, 270))



screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")

screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")


game_on = True
while game_on:
    screen.update()





screen.exitonclick()