from turtle import Screen
import time
from centerLine import CenterLine
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard

# TODO : 1. Create the screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=1200, height=700)
screen.title("Legend Pong Game")
screen.tracer(0)
centerline = CenterLine()

# TODO : 2. Create and move a paddle
# TODO : 3. Create another paddle
user1 = Paddle((-580, 0))
user2 = Paddle((580, 0))
screen.listen()
screen.onkey(user1.up, "w")
screen.onkey(user1.down, "s")
screen.onkey(user2.up, "Up")
screen.onkey(user2.down, "Down")

# TODO : 4. Create the ball and make it move
ball = Ball()

user1_score = 0
user2_score = 0
scoreboard = ScoreBoard()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.02)
    ball.move()

    # TODO : 5. Detect collision with wall and bounce
    if ball.ycor() > 300 or ball.ycor() < -300:
        ball.bounce_y()

    # TODO : 6. Detect collision with paddle
    if ball.distance(user1) < 50 and ball.xcor() < -560:
        ball.bounce_x()
    elif ball.distance(user2) < 50 and ball.xcor() > 560:
        ball.bounce_x()

    # TODO : 7. Detect when paddle misses
    # TODO : 8. Keep Score
    if ball.xcor() > 600:
        ball.reset_position()
        scoreboard.clear()
        scoreboard.user1_point()

    elif ball.xcor() < -600:
        ball.reset_position()
        scoreboard.clear()
        scoreboard.user2_point()




screen.exitonclick()
