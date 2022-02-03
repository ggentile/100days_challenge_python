from turtle import Turtle


class Turt(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.goto(0, -280)
        self.setheading(90)

    def up(self):
        self.setheading(90)
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        self.setheading(270)
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

    def left_pos(self):
        self.setheading(180)
        new_x = self.xcor() - 20
        self.goto(new_x, self.ycor())

    def right_pos(self):
        self.setheading(0)
        new_x = self.xcor() + 20
        self.goto(new_x, self.ycor())

    def initial_state(self):
        self.penup()
        self.goto(0, - 280)
        self.setheading(90)
