from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from score import Score_board
import time


# creating the paddles and the ball
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score_board = Score_board()
# the screen setup

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("pong")
screen.tracer(0)

# the game controls

screen.listen()
# the right paddle 
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

# the left paddle  
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detecting the collision with walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        # it will bounce
        ball.bounce_y()

    # Detecting the collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320 :
        ball.bounce_x()

    # detecting r_paddle misses
    if ball.xcor() > 380 : 
        ball.reset_position()
        score_board.l_point()
    
    
    # detecting l_paddle misses
    if ball.xcor() < -380 : 
        ball.reset_position()
        score_board.r_point()
    
    
    
screen.exitonclick()
