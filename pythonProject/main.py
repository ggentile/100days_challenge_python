import turtle as turtle_module
import random

turtle_module.colormode(255)
color_list = [(246, 245, 243), (233, 239, 246), (246, 239, 242),
              (240, 246, 243), (132, 166, 205), (221, 148, 106),
              (32, 42, 61), (199, 135, 148), (166, 58, 48),
              (141, 184, 162), (39, 105, 157), (237, 212, 90),
              (150, 59, 66), (216, 82, 71), (168, 29, 33),
              (235, 165, 157), (51, 111, 90), (35, 61, 55),
              (156, 33, 31), (17, 97, 71), (52, 44, 49),
              (230, 161, 166), (170, 188, 221), (57, 51, 48),
              (184, 103, 113), (32, 60, 109), (105, 126, 159),
              (175, 200, 188), (34, 151, 210), (65, 66, 56)]

tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for x in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if x % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()

