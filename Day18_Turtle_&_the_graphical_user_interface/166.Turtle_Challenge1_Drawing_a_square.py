#Drawing a square with turtle module

from turtle import Turtle, Screen
import turtle

timmy= Turtle()

for steps in range(4):
    timmy.forward(100)
    timmy.right(90)

screen=Screen()
screen.exitonclick()