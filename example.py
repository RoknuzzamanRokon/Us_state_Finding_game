import turtle

# Create the turtle screen and set its size
screen = turtle.Screen()
screen.setup(width=500, height=500)

# Set the background color of the screen
screen.bgcolor("lightblue")

s = turtle.Screen()# Rescale the screen coordinates to match the new screen size
s.setworldcoordinates(100,100,10,10)

# Use screen.textinput() to create a pop-up window with input field
name = screen.textinput("Enter your name", "What is your name?")

# Resize the pop-up window
s.textinput("Resize", "Press Enter to resize the window",800)

# Resize the turtle graphics window
screen.setup(width=800, height=800)
