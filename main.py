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
    answer = screen.textinput(f"Guess the State {len(guessed_state)}/50", "What's another state's name? ")
    answer = answer.title()
    if answer == "Exit":
        break
    if answer in states:
        guessed_state.append(answer)
        row = data[data.state == answer]
        turtle.goto(int(row.x), int(row.y))
        turtle.write(arg=f"{answer}", align=ALIGNMENT, font=FONT)

