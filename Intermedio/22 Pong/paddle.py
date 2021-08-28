from turtle import Turtle

MOVEMENT = 30


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.setpos(position, 0)
        self.shapesize(stretch_wid=5, stretch_len=1)

    def up(self):
        current = self.pos()

        if current[1] < 250:
            self.setpos(current[0], current[1] + MOVEMENT)

    def down(self):
        current = self.pos()

        if current[1] > -250:
            self.setpos(current[0], current[1] - MOVEMENT)
