#Day21
from turtle import Turtle ,Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
pong_ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")  
screen.onkey(r_paddle.go_down,"Down") 

screen.onkey(l_paddle.go_up, "w")  
screen.onkey(l_paddle.go_down,"s") 

game_is_on= True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    pong_ball.move()

    #----Detect collition with upper and lower wall
    if pong_ball.ycor() > 280 or pong_ball.ycor() < -280:
        pong_ball.bounce_y()

    #-----detect collision with both paddle
    if pong_ball.distance(r_paddle) < 50 and pong_ball.xcor() > 320 or pong_ball.distance(l_paddle) < 50 and pong_ball.xcor() < -320:
        pong_ball.bounce_x()

    #-----detect if r_paddle missed the ball
    if pong_ball.xcor() > 380 :
        pong_ball.reset_position()
        score.l_point()

    #-----detect if l_paddle missed the ball
    if pong_ball.xcor() < -380:
        pong_ball.reset_position()
        score.r_point()

screen.exitonclick()           