from turtle import Turtle

FONT=("Arial",20,"normal")

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.level=1
        
        self.hideturtle()
        self.penup()
        self.goto(-280,249)
        self.update_scoreboard()
    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}",align="left",font=FONT) #we defined font as a CONSTANT

    def increase_level(self):
        self.level+=1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over",align="center",font=FONT)