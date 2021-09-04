import turtle

SHAPE = "blank_states_img.gif"
TITLE = "Name the states"
PROMPT = "What's another state's name?"
TEXT = "States correct"


class GameManager:
    def __init__(self):
        self.correct = 0
        self.pantalla = turtle.Screen()
        self.pantalla.addshape(SHAPE)
        self.pantalla.title(TITLE)
        self.tortuga = turtle.Turtle()
        self.tortuga.hideturtle()
        self.tortuga.penup()
        turtle.shape(SHAPE)

    def ask_for_answer(self):
        window_title = f"{self.correct}/50 {TEXT}"
        answer = self.pantalla.textinput(title=window_title, prompt=PROMPT)
        return "" if answer is None else answer

    def is_playing(self):
        return self.correct < 50

    def score(self, xcor, ycor, state):
        self.correct += 1
        self.tortuga.goto(xcor, ycor)
        self.tortuga.write(state, align="center", font=("Arial", 12, "normal"))

    def win_game(self):
        self.tortuga.goto(0, 253)
        self.tortuga.write("Congratulations!", align="center", font=("Arial", 20, "normal"))
        turtle.mainloop()
