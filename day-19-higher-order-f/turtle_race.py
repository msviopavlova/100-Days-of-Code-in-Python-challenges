from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
print(user_bet)

tim = Turtle(shape="turtle")
tim.penup()
tim.color("red")
tim.goto(x=-230, y=-100)


lappi = Turtle(shape="turtle")
lappi.penup()
lappi.color("purple")
lappi.goto(x=-230, y=-50)


fox = Turtle(shape="turtle")
fox.penup()
fox.color("orange")
fox.goto(x=-230, y=0)

lol = Turtle(shape="turtle")
lol.penup()
lol.color("yellow")
lol.goto(x=-230, y=50)

boobaloo = Turtle(shape="turtle")
boobaloo.penup()
boobaloo.color("blue")
boobaloo.goto(x=-230, y=100)


jack = Turtle(shape="turtle")
jack.penup()
jack.color("green")
jack.goto(x=-230, y=150)



screen.exitonclick()