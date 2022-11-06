from msilib.schema import Class
from turtle import Turtle
STARTING_POSITON=(0,-200)
MOVE_DISTANCE=10
FINISH_LINE_Y=200

class Player(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITON)
        self.setheading(90)
        self.y_move=10

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def go_to_start(self):
        self.goto(STARTING_POSITON)
    
    def is_at_finish_line(self):
        if self.ycor()>FINISH_LINE_Y:
            return True
        else:
            return False
