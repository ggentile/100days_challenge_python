import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
turtle.addshape(image)

turtle.shape(image)


data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guesses = []


while len(guesses) < 50:
    answer = screen.textinput(title=f"{len(guesses)}/50 States Correct",
                              prompt="What's another state's name?").title()

    if answer == "Exit":
        missing_states = [state for state in all_states if state not in guesses]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer in all_states:
        guesses.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer)
