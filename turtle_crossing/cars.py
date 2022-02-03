from turtle import Turtle
import random


class Cars(Turtle):

    FORWARD_SPEED = 5

    car_colors = ["dark sea green", "light blue", "orange red", "dark magenta",
                  "light slate gray", "turquoise", "honeydew", "yellow",
                  "peach puff", "lavender blush"]

    def __init__(self):
        self.all_cars = []

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.setheading(180)
            new_car.color(random.choice(Cars.car_colors))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.forward(Cars.FORWARD_SPEED)

    def increase_difficulty(self):
        Cars.FORWARD_SPEED += 2
        print(Cars.FORWARD_SPEED)
