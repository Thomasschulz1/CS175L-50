import math
import turtle

# Named constants
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
ANIMATION_SPEED = 0
NUM_SIDES = 8
LENGTH = 100
ANGLE = 45
TEXT_X = -5
TEXT_Y = -10

# Size the window.
turtle.setup(WINDOW_WIDTH, WINDOW_HEIGHT)

# Calculate the diameter of the octagon so we
# can center it in the graphics window.
#                s
#        ---------------
#       / |             \
#  s   /  |              \
#     /   | x             \  s
#    /    |                \
#   |------                 |
#   |   x                   |
#   |                       |
#   To get the diameter:
#     diameter = s + 2 * x
#   We know that s is 100.
#   Use Pythagoras to get x:
#   s^2 = x^2 + x^2
#   s^2 = 2*x^2
#   x = s / sqrt(2)
s = LENGTH
x = s / math.sqrt(2)
diameter = s + (2 * x)
Greg = turtle.Turtle()
Greg.color('white')
Greg.penup()
Greg.setposition(-55,-70)
Greg.pendown()
turtle.hideturtle()
turtle.bgcolor('red')
Greg.color('white')
word_font = ('Arial', 90, 'bold')
turtle.write('STOP', font = word_font, align = 'center')
Greg.pencolor('white')
for x in range(8):
    Greg.forward(100)
    Greg.left(45)
turtle.done()
