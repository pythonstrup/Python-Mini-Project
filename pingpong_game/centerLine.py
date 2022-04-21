from turtle import Turtle
XPOS = 0
YPOS = 350
SOUTH = 270
DIST = 20


class CenterLine(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.setpos(XPOS, YPOS)
        self.setheading(SOUTH)
        self.pencolor("white")
        while self.ycor() > -YPOS:
            self.pendown()
            self.forward(DIST)
            self.penup()
            self.forward(DIST)