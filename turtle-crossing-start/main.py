import random
import time
from turtle import Screen
from player import Player
from scoreboard import Scoreboard
from car_manager import CarManager


player = Player()


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


car_creator = CarManager()

screen.listen()
screen.onkey(player.move_up, "Up")

game_is_on = True

while game_is_on:

    time.sleep(0.1)
    screen.update()

    car_creator.creating_car()
    car_creator.keep_moving()

    for car in car_creator.all_cars:
        if player.distance(car) < 20:
            game_is_on = False


    if player.is_at_finishline():
        player.go_back_to_start()
        car_creator.level_up()




