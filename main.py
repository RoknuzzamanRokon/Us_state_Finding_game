import turtle


screen = turtle.Screen()
screen.title("U.S states game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

display = screen.textinput(title="us states find game.", prompt="Right a us-stat name.")

# def click_on_display(x, y):
#     print(x, y)
#
# turtle.onscreenclick(click_on_display)

screen.mainloop()

