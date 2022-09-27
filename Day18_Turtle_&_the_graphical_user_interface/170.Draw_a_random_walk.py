
from shutil import move
from turtle import Turtle, Screen
import random


mini_turtle=Turtle()
mini_turtle.shape("turtle")
angle_list=[0,90,180,270]
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

for steps in range(200):
    mini_turtle.color(random.choice(colours))
    mini_turtle.pensize(10)
    mini_turtle.speed("fastest")
    mini_turtle.forward(30)
    mini_turtle.setheading(random.choice(angle_list)) #Chose a random direction from angle list

screen=Screen()
screen.exitonclick()