from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
scoreboard = Scoreboard()
ball = Ball()
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
game_is_on = True
while game_is_on :
    time.sleep(0.1)
    screen.update()
    ball.move()
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 and ball.x_move > 0 :
        ball.bounce_x()
    if ball.distance(l_paddle) < 50 and ball.xcor() < -320 and ball.x_move < 0:
        ball.bounce_x()
    if ball.xcor() > 380 :
        ball.reset_position()
        scoreboard.l_point()
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
    if ball.ycor() > 280 or ball.ycor() < -280 :
        ball.bounce_y()

screen.exitonclick()
