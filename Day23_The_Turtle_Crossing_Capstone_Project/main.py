import time
from turtle import Screen
from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard
screen=Screen()
screen.setup(600,600)
screen.tracer(0) #Turns turtle animation

player=Player()
car_manager= CarManager()
scoreboard= Scoreboard()

screen.listen()
screen.onkeypress(player.move_up,"Up")
game_is_on=True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_cars()
    car_manager.move_cars()

    #Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player)<20:
            game_is_on=False        #If detect collision, the game will finish
            scoreboard.game_over()
    #Detect succesful crossing
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()
        
screen.exitonclick()    