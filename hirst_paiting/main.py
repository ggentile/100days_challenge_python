from turtle import Screen, Turtle, forward
import random


colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
timmy_the_turtle = Turtle()

timmy_the_turtle.shape('turtle')
timmy_the_turtle.color('purple')

lados = 3
forward = 100
index = 1

def angle(lados):
    circle = 360
    value = circle / lados
    return value

def quantidade_voltas(numero_loops):
    resultado = numero_loops + 2
    return resultado

for x in range(8):
    y = angle(lados)
    timmy_the_turtle.color(random.choice(colors))
    voltas = quantidade_voltas(index)
    for num in range(voltas):
        timmy_the_turtle.left(y)
        timmy_the_turtle.forward(forward)
    lados += 1
    forward += 10
    index += 1













screen = Screen()
screen.exitonclick()