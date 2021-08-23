from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

is_alive = True

pantalla = Screen()
pantalla.setup(width=600, height=600)
pantalla.bgcolor("black")
pantalla.title("Snake Game")
pantalla.tracer(0)

pantalla.listen()
serpiente = Snake()
comida = Food()
puntos = ScoreBoard()

pantalla.onkey(serpiente.right, "Right")
pantalla.onkey(serpiente.down, "Down")
pantalla.onkey(serpiente.up, "Up")
pantalla.onkey(serpiente.left, "Left")

pantalla.update()

while is_alive:
    pantalla.update()
    time.sleep(0.1)
    serpiente.move()

    if serpiente.head.distance(comida) < 15:
        comida.refresh()
        serpiente.increase()
        puntos.print_score()

    if serpiente.head.xcor() > 280 or serpiente.head.xcor() < -280\
            or serpiente.head.ycor() > 280 or serpiente.head.ycor() < -280:
        puntos.game_over()
        is_alive = False

    for segment in serpiente.parts[1:]:
        if serpiente.head.distance(segment) < 10:
            puntos.game_over()
            is_alive = False

pantalla.exitonclick()
