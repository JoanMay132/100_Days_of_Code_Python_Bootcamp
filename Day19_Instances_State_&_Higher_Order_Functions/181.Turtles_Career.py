'''Turtle career'''

from turtle import Turtle, Screen
import random
import turtle
screen=Screen()

screen.setup(width=500,height=400)

x_positions=[-180,-120,-60,0,60,120]
colors=["red","orange","yellow","green","blue","purple"]

user_bet= screen.textinput(title=" Make your bet!",prompt="Which turtle will win the raice? Make your bet:")

is_race_on=False
all_turtle=[]
for turtle_index in range(1,6):
    new_turtle=Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.setheading(90)
    new_turtle.penup()
    new_turtle.goto(x=x_positions[turtle_index],y=-150)
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on=True

while is_race_on:
    
    for turtle in all_turtle:
        if turtle.ycor() > 180:
            is_race_on=False 
            winning_color=turtle.pencolor()
            if winning_color==user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        rand_distance=random.randint(0,10)
        turtle.forward(rand_distance)



screen.exitonclick()