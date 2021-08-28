from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.print_score()

    def print_score(self):
        self.clear()
        self.goto(-100, 190)
        self.write(self.left_score, align="center", font=("Corier", 80, "normal"))
        self.goto(100, 190)
        self.write(self.right_score, align="center", font=("Corier", 80, "normal"))

    def score(self, left=True):
        if left:
            self.left_score += 1
        else:
            self.right_score += 1
