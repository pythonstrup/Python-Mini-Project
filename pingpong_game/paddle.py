from turtle import Turtle
NORTH = 90
SOUTH = 270
A, B = 5, 1

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.goto(position)
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=A, stretch_len=B)

    def up(self):
        if self.ycor() < 300:
            new_ypos = self.ycor() + 30
            self.goto(self.xcor(), new_ypos)

    def down(self):
        if self.ycor() > -300:
            new_ypos = self.ycor() - 30
            self.goto(self.xcor(), new_ypos)

