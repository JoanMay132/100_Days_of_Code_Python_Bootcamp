from turtle import Turtle, Screen, forward
import random
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

mini_turtle= Turtle()

def draw_shape(num_sides):
    angle=360/num_sides
    for steps in range(num_sides):
        mini_turtle.forward(100)
        mini_turtle.right(angle)

for shape_side_n in range(3,11):
    mini_turtle.color(random.choice(colours))
    draw_shape(shape_side_n)


screen=Screen()
screen.exitonclick