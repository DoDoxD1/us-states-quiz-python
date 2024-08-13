from turtle import Turtle, Screen
import pandas

ALIGNMENT = "center"
FONT = ("arial", 8, "normal")

guessed_state = []

# set up the screen
screen = Screen()
screen.title("US State Quiz")
screen.bgpic("blank_states_img.gif")

turtle = Turtle()
turtle.penup()
turtle.hideturtle()

data = pandas.read_csv("50_states.csv")
states = data.state.to_list()

while len(guessed_state) < 50:

    # getting user input
    answer = screen.textinput(f"Guess the State {len(guessed_state)}/50", "What's another state's name? ").title()

    # user wants to exit
    if answer == "Exit":
        s1 = set(states)
        s2 = set(guessed_state)
        diff = list(s1 - s2)
        states_to_learn = pandas.DataFrame(diff)
        states_to_learn.to_csv("states_to_learn.csv")
        break

    # checking if guessed answer is correct and exist in data
    if answer in states:

        # adding to guessed answers list
        guessed_state.append(answer)

        # getting the coordinates and writing the state names
        row = data[data.state == answer]
        turtle.goto(int(row.x), int(row.y))
        turtle.write(arg=f"{answer}", align=ALIGNMENT, font=FONT)
