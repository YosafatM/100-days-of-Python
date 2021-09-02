from turtle import Turtle

SPEED = 20


class Snake:
    def __init__(self):
        t = Turtle(shape="square")
        t.color("white")
        t.penup()

        self.parts = [t, t.clone(), t.clone()]
        self.parts[1].goto(x=-20, y=0)
        self.parts[2].goto(x=-40, y=0)
        self.direction = "right"
        self.head = self.parts[0]

    def up(self):
        if self.direction != "down":
            self.direction = "up"

    def down(self):
        if self.direction != "up":
            self.direction = "down"

    def left(self):
        if self.direction != "right":
            self.direction = "left"

    def right(self):
        if self.direction != "left":
            self.direction = "right"

    def increase(self):
        tortuga = self.parts[-1].clone()
        self.parts.append(tortuga)

    def move(self):
        for index in range(len(self.parts)-1, 0, -1):
            self.parts[index].setposition(self.parts[index - 1].pos())

        pos_x = self.head.xcor()
        pos_y = self.head.ycor()

        if self.direction == "up":
            self.head.setposition(pos_x, pos_y + SPEED)
        elif self.direction == "down":
            self.head.setposition(pos_x, pos_y - SPEED)
        elif self.direction == "right":
            self.head.setposition(pos_x + SPEED, pos_y)
        else:
            self.head.setposition(pos_x - SPEED, pos_y)

    def reset(self):
        for piece in self.parts:
            piece.goto(1000, 1000)

        t = Turtle(shape="square")
        t.color("white")
        t.penup()

        self.parts = [t, t.clone(), t.clone()]
        self.parts[1].goto(x=-20, y=0)
        self.parts[2].goto(x=-40, y=0)
        self.direction = "right"
        self.head = self.parts[0]
