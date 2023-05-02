import turtle
import pandas


screen = turtle.Screen()
screen.title("U.S. states game")
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_state = data.state.to_list()
guessed_state = []


while len(guessed_state) < 50:
    user_data = screen.textinput(f"You Guessed:{len(guessed_state)}/50",
                                 "\t\tWrite a US state name\t\t").title()

    if user_data in all_state:
        guessed_state.append(user_data)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data['state'] == user_data]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(user_data)

screen.mainloop()

