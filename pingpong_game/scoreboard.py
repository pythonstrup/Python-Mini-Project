from turtle import Turtle

FONT = ("Courier", 50, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('white')
        self.user1 = 0
        self.user2 = 0
        self.update()


    def update(self):
        self.goto(-150, 250)
        self.write(f"{self.user1}", font=FONT)
        self.goto(100, 250)
        self.write(f"{self.user2}", font=FONT)

    def user1_point(self):
        self.user1 += 1
        self.update()

    def user2_point(self):
        self.user2 += 1
        self.update()
