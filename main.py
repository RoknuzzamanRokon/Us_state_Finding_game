import turtle
import pandas as pd


screen = turtle.Screen()
screen.title("U.S states game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

read_csv_file = pd.read_csv('50_states.csv')
all_state = read_csv_file.state.to_list()

make_list = 0


while make_list < 50:
    display = screen.textinput(title=f"Your score:{make_list}/50", prompt="wright a us-stat name.").capitalize()

    if display in all_state:
        make_list += 1
        print(make_list)
        read_state = read_csv_file[read_csv_file['state'] == display]
        make_dict = read_state.to_dict()
        position = (list(make_dict['x'].values())[0], list(make_dict['y'].values())[0])
        name = (list(make_dict['state'].values())[0])

        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(position)
        t.write(name, align="center", font=('Arial', 10, 'normal'))
    # def click_on_display(x, y):
    #     print(x, y)
    #
    # turtle.onscreenclick(click_on_display)

# screen.mainloop()
screen.exitonclick()
