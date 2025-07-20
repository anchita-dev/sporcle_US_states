import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed = []

while len(guessed) < 50:
    answer = screen.textinput(title=f"{len(guessed)}/50 States Correct", prompt="What's another state's name?").title()

    if answer == "Exit":
        missing = [state for state in all_states if state not in guessed]
        # for state in all_states:
        #     if state not in guessed:
        #         missing.append(state)

        new_data = pandas.DataFrame(missing)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer in all_states:
        guessed.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer)


