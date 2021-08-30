from turtle import Turtle
import random as rd

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
STARTING_PROBABILITY = 5
Y_LIMIT = 250


class CarManager:
    def __init__(self):
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE
        self.probability = STARTING_PROBABILITY

    def move_cars(self):
        self.random_generator()

        for car in self.cars:
            position = car.pos()
            car.goto(position[0] - self.speed, position[1])

            if car.pos()[0] < -320:
                self.cars.remove(car)

    def random_generator(self):
        number = rd.randint(0, self.probability)

        if number == 0:
            car = Turtle(shape="square")
            car.turtlesize(stretch_wid=1, stretch_len=2)
            car.color(rd.choice(COLORS))
            car.penup()
            car.goto(320, rd.randint(-Y_LIMIT, Y_LIMIT))
            self.cars.append(car)

    def collide(self, player):
        for car in self.cars:
            p1 = car.pos()
            p2 = player.pos()

            if p1[0]-23 < p2[0] < p1[0]+23 and p1[1]-18 < p2[1] < p1[1]+18:
                return True

        return False

    def next_level(self):
        if self.probability > 1:
            self.probability = self.probability - 1

        self.speed += MOVE_INCREMENT
