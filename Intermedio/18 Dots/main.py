from turtle import Turtle, Screen
import random as rd
# import colorgram
#
# colors = colorgram.extract("image.jpg", 30)
# rgb = []
#
# for color in colors:
#     r = color.rgb[0]
#     g = color.rgb[1]
#     b = color.rgb[2]
#     rgb.append((r, g, b))

color_list = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136),
              (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86),
              (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50),
              (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19),
              (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

tortuga = Turtle()
pantalla = Screen()

y = -200
pantalla.colormode(255)
tortuga.penup()
tortuga.setx(-200)
tortuga.sety(y)

for _ in range(10):
    for _ in range(10):
        tortuga.dot(15, rd.choice(color_list))
        tortuga.forward(50)

    tortuga.setx(-200)
    y += 50
    tortuga.sety(y)

pantalla.exitonclick()
