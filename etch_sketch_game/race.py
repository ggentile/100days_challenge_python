import random
from turtle import Turtle, Screen
import turtle

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title='make your bet', prompt='Select the turtle you wanna bet on: ')
color = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
y_positions = [-70, -40, -10, 20, 50, 80]
all_turts = []

for col in range(0, 6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(color[col])
    new_turtle.penup()

    new_turtle.goto(x=-220, y=y_positions[col])
    all_turts.append(new_turtle)


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turts:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won! The {winning_color} turtle is the winner!")
            else:
                print(f"You lost!")
        distance = random.randint(0,10)
        turtle.forward(distance)

screen.exitonclick()

