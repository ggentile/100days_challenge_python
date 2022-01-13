from turtle  import Screen, Turtle
import random

colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

spyro = Turtle()

spyro.color(random.choice(colors))
spyro.pensize(2)
spyro.speed("fastest")

for _ in range(100):
    spyro.color(random.choice(colors))
    spyro.circle(100)
    spyro.left(10)
    spyro.hideturtle()


screen = Screen()
screen.exitonclick()