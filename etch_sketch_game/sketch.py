from turtle import Turtle, Screen


game = True
tim = Turtle()

screen = Screen()


def move_forward():
    tim.forward(10)

def move_backwards():
    tim.back(10)

def move_counter_clockwise():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def move_clockwise():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def clean_screen():
    tim.clear()

while game == True:
    screen.listen()
    screen.onkeypress(key="w", fun=move_forward)
    screen.onkeypress(key="s", fun=move_backwards)
    screen.onkeypress(key="a", fun=move_counter_clockwise)
    screen.onkeypress(key="d", fun=move_clockwise)
    screen.onkey(key="c", fun=clean_screen)
    if screen.exitonclick():
        game = False




screen.exitonclick()
