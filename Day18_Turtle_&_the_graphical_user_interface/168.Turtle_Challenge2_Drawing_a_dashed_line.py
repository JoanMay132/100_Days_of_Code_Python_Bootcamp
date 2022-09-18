from turtle import Turtle, Screen 

timmy_turtle= Turtle()

for steps in range(15):
    timmy_turtle.forward(10)
    timmy_turtle.penup()
    timmy_turtle.forward(10)
    timmy_turtle.pendown()


screen=Screen()
screen.exitonclick()