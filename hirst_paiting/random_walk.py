import random
from turtle  import Screen, Turtle


colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
choice = ['heads', 'tails']
directions = [0, 90, 180, 270]

tim = Turtle()

tim.shape('arrow')
tim.color(colors[1])
tim.pensize(10)
tim.speed(10)

for _ in range(200):
    tim.color(random.choice(colors))
    tim.forward(30)
    tim.setheading(random.choice(directions))





screen = Screen()
screen.exitonclick()