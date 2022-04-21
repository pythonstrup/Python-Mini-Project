from turtle import Turtle
import random
SPEED = 10


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.x = random.choice([-SPEED, SPEED])
        self.y = random.choice([-SPEED, SPEED])


    def move(self):
        new_x = self.xcor() + self.x
        new_y = self.ycor() + self.y
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y *= -1

    def bounce_x(self):
        self.x *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()