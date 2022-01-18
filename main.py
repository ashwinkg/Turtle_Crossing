from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import ScoreBoard
import time

FINISH_LINE_Y = 280

my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.tracer(0)

player = Player()
scoreboard = ScoreBoard()

my_screen.listen()
my_screen.onkeypress(key="Up", fun=player.move_up)
my_screen.onkeypress(key="Down", fun=player.move_down)

car_manager = CarManager()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    my_screen.update()

    car_manager.create_car()
    car_manager.move_car()

    # Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.print_game_over()
            game_is_on = False

    # Detect turtle crossed finish line
    if player.is_at_finish_line():
        car_manager.level_up()
        scoreboard.update_level()

my_screen.exitonclick()
