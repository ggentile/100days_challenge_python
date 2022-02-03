from turtle import Turtle


class Level(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.update_level()

    def update_level(self):
        self.clear()
        self.goto(-230, 260)
        self.write("Level: ", align="center", font=("Courier", 15, "normal"))
        self.goto(-190, 260)
        self.write(self.level, align="center", font=("Courier", 15, "normal"))

    def next_level(self):
        self.level += 1
        self.update_level()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Courier", 15, "normal"))

    def initial_level(self):
        self.level = 1
        self.update_level()
