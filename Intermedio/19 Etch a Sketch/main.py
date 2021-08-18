from turtle import Turtle, Screen


def l_up():
    tortuga.forward(20)


def l_down():
    tortuga.backward(20)


def l_left():
    tortuga.left(5)


def l_right():
    tortuga.right(5)


def l_clear():
    tortuga.goto(0, 0)
    tortuga.clear()


tortuga = Turtle()
pantalla = Screen()

pantalla.listen()
pantalla.onkey(l_up, "W")
pantalla.onkey(l_down, "S")
pantalla.onkey(l_left, "A")
pantalla.onkey(l_right, "D")

pantalla.onkey(l_up, "w")
pantalla.onkey(l_down, "s")
pantalla.onkey(l_left, "a")
pantalla.onkey(l_right, "d")

pantalla.onkey(l_clear, "C")
pantalla.onkey(l_clear, "c")

pantalla.exitonclick()
