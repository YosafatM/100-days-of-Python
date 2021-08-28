from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

pantalla = Screen()
pantalla.setup(width=800, height=600)
pantalla.bgcolor("black")
pantalla.title("Pong")

pantalla.tracer(0)
player_2 = Paddle(350)
player_1 = Paddle(-350)
ball = Ball()
scoreboard = Scoreboard()

pantalla.listen()
pantalla.onkeypress(player_2.up, "P")
pantalla.onkeypress(player_2.down, "L")
pantalla.onkeypress(player_2.up, "p")
pantalla.onkeypress(player_2.down, "l")
pantalla.onkeypress(player_1.up, "W")
pantalla.onkeypress(player_1.down, "S")
pantalla.onkeypress(player_1.up, "w")
pantalla.onkeypress(player_1.down, "s")

while True:
    time.sleep(ball.frame)
    pantalla.update()
    ball.move()

    if ball.xcor() >= 330 and ball.should_bounce(player_2):
        ball.bounce()

    if ball.xcor() <= -330 and ball.should_bounce(player_1):
        ball.bounce()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.score(left=True)
        scoreboard.print_score()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.score(left=False)
        scoreboard.print_score()
