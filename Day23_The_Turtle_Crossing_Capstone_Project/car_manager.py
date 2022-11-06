

from turtle import Turtle
import random
COLOR=["red","orange","yellow","green","blue","purple"]
STARTING_MOVE_DISTANCE=5
MOVE_INCREMENT=10

class CarManager:
    def __init__(self):
        self.all_cars=[]
        self.car_speed= STARTING_MOVE_DISTANCE
    def create_cars(self):
        random_chance=random.randint(1,3)
        if random_chance==1: #generating a random car
            new_car=Turtle("square")
            new_car.shapesize(stretch_wid=1,stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLOR))
            #Defining where it's going to go on the screen
            random_y=random.randint(-250,300)
            #Go to the x position
            new_car.goto(300,random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    
    def level_up(self):
        self.car_speed+=MOVE_INCREMENT