from turtle import Turtle, Screen
import shapes
import random as rd

tortuga = Turtle()
pantalla = Screen()
pantalla.colormode(255)

for i in range(3, 10):
    tortuga.pencolor(rd.randint(1, 255), rd.randint(1, 255), rd.randint(1, 255))
    shapes.regular_shape(tortuga, 100, i, line=shapes.solid_line)

pantalla.exitonclick()
