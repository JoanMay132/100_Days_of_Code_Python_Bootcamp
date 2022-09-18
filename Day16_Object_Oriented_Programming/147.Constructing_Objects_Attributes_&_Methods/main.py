"""We are going to be creating an object from a blueprint that somebody else has created."""
import another_module
print(another_module.another_variable)


import turtle

timmy=turtle.Turtle() # Create a class object which is .Turtle()

#or we can use the following: 
from turtle import Turtle, Screen #This is our new object, another class is screen(represents the windows in wich the turtle is going to be show up)
timmy=Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("SlateBlue1")
timmy.left(900)
timmy.forward(100)
my_screen=Screen() #This is our new object, another class is screen(represents the windows in wich the turtle is going to be show up)
print(my_screen.canvheight) #.canvheight is a method that we can use to get the height of the screen (attributes)

my_screen.exitonclick() #This is a method that we can use to close the screen when we click on it