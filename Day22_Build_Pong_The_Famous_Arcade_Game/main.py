from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time
screen=Screen()



screen.bgcolor("black")
screen.setup(800,600)
screen.title("Pong")
screen.tracer(0)

r_paddle=Paddle((350,0))
left_paddle=Paddle((-350,0))

ball=Ball()
scoreboard = ScoreBoard()

screen.listen()
screen.onkeypress(r_paddle.go_up,"Up")
screen.onkeypress(r_paddle.go_down,"Down")
screen.onkeypress(left_paddle.go_up,"w")
screen.onkeypress(left_paddle.go_down,"s")


game_is_on=True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # Detect collision with wall
    if ball.ycor()>280 or ball.ycor()<-280:
        #needs to bounce
        ball.bounce_y()
    #Detect collision with right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor()>320 or ball.distance(left_paddle)<50 and ball.xcor()<-320:
        ball.bounce_x()

    # Detect when right paddle misses
    if ball.xcor()>380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect when left paddle misses
    if ball.xcor()<-380:
        ball.reset_position()
        scoreboard.r_point()
        
screen.exitonclick()