import turtle

screen = turtle.Screen()
screen.title("U.S states game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


def click_on_display(x, y):
    print(x, y)


turtle.onscreenclick(click_on_display)


screen.mainloop()

