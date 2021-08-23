from turtle import Screen
import time
from snake import Snake

is_alive = True

pantalla = Screen()
pantalla.setup(width=600, height=600)
pantalla.bgcolor("black")
pantalla.title("Snake Game")
pantalla.tracer(0)

pantalla.listen()
serpiente = Snake()
pantalla.onkey(serpiente.right, "Right")
pantalla.onkey(serpiente.down, "Down")
pantalla.onkey(serpiente.up, "Up")
pantalla.onkey(serpiente.left, "Left")

pantalla.update()

while is_alive:
    pantalla.update()
    time.sleep(0.1)
    serpiente.move()

pantalla.exitonclick()
