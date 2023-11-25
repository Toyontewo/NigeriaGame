import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("Nigeria States game")
image = "Map2.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("States_coor.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 36:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/36 States Correct",
                                    prompt="What's another state name?").title()

    if answer_state == "Exit":
        missing_state = []

        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)


# turtle.mainloop()