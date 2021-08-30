import time
from turtle import Screen
from player import Player, FINISH_LINE_Y
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.listen()
screen.tracer(0)

player = Player()
car_manager = CarManager()
screen.onkeypress(player.up, "Up")
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.move_cars()

    if car_manager.collide(player):
        scoreboard.game_over()
        screen.update()
        break

    if player.pos()[1] > FINISH_LINE_Y:
        player.new_level()
        car_manager.next_level()
        scoreboard.next_level()

screen.exitonclick()