from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = -1
        self.next_level()

    def next_level(self):
        self.score += 1
        text = f"Level: {self.score}"
        self.goto(-215, 260)
        self.clear()
        self.write(text, align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.clear()
        self.write("GAME OVER", align="center", font=FONT)
