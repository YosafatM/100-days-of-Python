from turtle import Turtle, Screen
import shapes
import random as rd

pantalla = Screen()
pantalla.colormode(255)

num = 100
tortugas = []

for _ in range(4):
    tortuga = Turtle()
    tortuga.speed(0)
    tortuga.hideturtle()
    tortuga.penup()
    tortugas.append(tortuga)

tortugas[0].goto(-20, -20)
tortugas[1].goto(20, -20)
tortugas[2].goto(-20, 20)
tortugas[3].goto(20, 20)

tortugas[0].setheading(225)
tortugas[1].setheading(315)
tortugas[2].setheading(135)
tortugas[3].setheading(45)

tortugas[0].pendown()
tortugas[1].pendown()
tortugas[2].pendown()
tortugas[3].pendown()

for i in range(0, int(num/3)):
    for tortuga in tortugas:
        angle = 360 / num
        tortuga.pencolor(rd.randint(1, 255), rd.randint(1, 255), rd.randint(1, 255))
        tortuga.right(angle)
        shapes.regular_shape(tortuga, 150, 3)

pantalla.exitonclick()
