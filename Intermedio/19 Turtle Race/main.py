from turtle import Turtle, Screen
import random as rd

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = -80
x_position = -230
tortugas = []
is_racing = True

screen = Screen()
screen.setup(width=500, height=400)
bet = screen.textinput(title="What's your bet?", prompt=f"Enter a color {colors}: ")

for color in colors:
    tortuga = Turtle(shape="turtle")
    tortuga.penup()
    tortuga.color(color)
    tortuga.goto(x=x_position, y=y_position)
    tortugas.append(tortuga)
    y_position += 30

while is_racing:
    for tortuga in tortugas:
        if tortuga.xcor() > 230:
            is_racing = False

            if tortuga.pencolor() == bet:
                print(f"You've won! The {tortuga.pencolor()} one is the winner!")
            else:
                print(f"You've lost. The {tortuga.pencolor()} one is the winner!")

        distance = rd.randint(0, 10)
        tortuga.forward(distance)

screen.exitonclick()
