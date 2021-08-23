from turtle import Turtle

STYLE = ("Arial", 12, "bold")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.score = -1
        self.print_score()

    def print_score(self):
        self.goto(0, 280)
        self.clear()

        self.score += 1
        cadena = f"Score: {self.score}"
        self.write(cadena, align="center", font=STYLE)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=STYLE)
