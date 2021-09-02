from turtle import Turtle

STYLE = ("Arial", 12, "bold")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.score = -1
        self.high_score = 0

        with open("data.txt") as file:
            self.high_score = int(file.read())

        self.print_score()

    def print_score(self):
        self.goto(0, 280)
        self.clear()

        self.score += 1
        cadena = f"Score: {self.score}  High Score: {self.high_score}"
        self.write(cadena, align="center", font=STYLE)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score

            with open("data.txt", mode="w") as file:
                file.write(str(self.high_score))

        self.score = 0
        self.print_score()
