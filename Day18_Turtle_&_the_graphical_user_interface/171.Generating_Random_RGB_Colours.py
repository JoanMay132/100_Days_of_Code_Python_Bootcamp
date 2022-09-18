'''

Python Tuples.
A tuple is a data type like this tuple=(1,2,3,4)
'''

from turtle import Turtle, Screen
import random

mini_turtle=Turtle()
screen=Screen()
screen.colormode(255)
mini_turtle.shape("turtle")
angle_list=[0,90,180,270]

def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    random_color=(r,g,b)
    return random_color




for steps in range(200):
    mini_turtle.color(random_color())
    mini_turtle.pensize(10)
    mini_turtle.speed("fastest")
    mini_turtle.forward(30)
    mini_turtle.setheading(random.choice(angle_list))

screen.exitonclick()