# turtle only works with .gif, not .png or .jpeg

import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
#lmao you forgot to turn this into a list. this is critical
correct_guesses = []


while len(correct_guesses) < 50:
    state_answer = screen.textinput(title=f"{len(correct_guesses)}/50 correct", prompt="Please name a state:").title()
    if state_answer == "Exit":
        missing_states = [state for state in all_states if state not in correct_guesses]
        # for state in states:
        #     if state not in correct_guesses:
        #         missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break


    #use 'in' keyword in order to check if something is in the list
    if state_answer in all_states:
        correct_guesses.append(state_answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == state_answer] #i got this right
        # x_coordinate = state_location["x"].to_list()
        # y_coordinate = state_location["y"].to_list()
        # turtle.goto(x_coordinate, y_coordinate)
        t.goto(int(state_data.x), int(state_data.y)) #i got this right too
        t.write(state_answer)


# states_to_learn.csv
