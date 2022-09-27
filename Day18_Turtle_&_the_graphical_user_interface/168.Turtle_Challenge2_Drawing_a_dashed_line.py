from turtle import Turtle, Screen 

timmy_turtle= Turtle()

for steps in range(15): #Move forward 10 px penup() and move forward 10 px againg and pendown()
    timmy_turtle.forward(10)
    timmy_turtle.penup()
    timmy_turtle.forward(10)
    timmy_turtle.pendown()


screen=Screen()
screen.exitonclick()