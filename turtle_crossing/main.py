from turtle import Screen
from turt import Turt
from cars import Cars
import time
from level import Level


screen = Screen()
screen.bgcolor("white")
screen.title("Turtle Cross")
screen.setup(width=600, height=600)
screen.tracer(0)

tim = Turt()
lvl = Level()
car = Cars()

screen.listen()
screen.onkey(tim.up, "w")
screen.onkey(tim.down, "s")
screen.onkey(tim.right_pos, "d")
screen.onkey(tim.left_pos, "a")


game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create_car()
    car.move()

    if tim.ycor() < -280:
        tim.undo()
    elif tim.xcor() > 280 or tim.xcor() < -280:
        tim.undo()

    if tim.ycor() == 280:
        tim.initial_state()
        lvl.next_level()
        car.increase_difficulty()

    for x in car.all_cars:
        if x.distance(tim) < 20:
            lvl.game_over()
            game_is_on = False

screen.exitonclick()
