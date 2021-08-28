from turtle import Turtle
import random as rd
import time

MOVEMENT = 5
FRAME_TIME = 0.02


class Ball(Turtle):
    def __init__(self):
        super().__init__(shape="circle")
        self.color("white")
        self.penup()
        self.x_speed = MOVEMENT
        self.y_speed = rd.randint(3, MOVEMENT)
        self.frame = FRAME_TIME
        self.last_bounce = time.time()

    def move(self):
        current = self.pos()

        if current[1] > 290 or current[1] < -290:
            self.y_speed = -self.y_speed

        self.setpos(current[0] + self.x_speed, current[1] + self.y_speed)

    def bounce(self):
        self.x_speed = -self.x_speed
        self.frame *= 0.9

    def should_bounce(self, paddle):
        p1 = self.pos()
        p2 = paddle.pos()

        if p2[1] - 50 < p1[1] < p2[1] + 50:
            if p2[0] < 0:
                return p2[0] + 20 == p1[0]
            else:
                return p2[0] - 20 == p1[0]

        return False

    def reset_position(self):
        self.goto(0, 0)
        self.frame = FRAME_TIME
        self.bounce()
