from turtle import Turtle, Screen

# set up the screen
screen = Screen()
screen.title("US State Quiz")
screen.bgpic("blank_states_img.gif")

# getting user input
answer = screen.textinput("Guess the State", "What's another state's name? ")

screen.exitonclick()
