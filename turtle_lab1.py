# turtle_lab1.py

'''import turtle
turtle.forward(100)
turtle.done()

# too cumbersom
from turtle import *
forward(100)
done()
'''

import turtle
# head
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
# move to neck
turtle.penup()
turtle.forward(25)
turtle.pendown()
# neck
turtle.right(90)
turtle.forward(35)
# right arm
turtle.left(115)
turtle.forward(35)
# back to neck
turtle.right(180)
turtle.penup()
turtle.forward(35)
# left arm
turtle.right(55)
turtle.pendown()
turtle.forward(35)
# back to neck
turtle.right(180)
turtle.penup()
turtle.forward(35)
turtle.right(60)
# body
turtle.pendown()
turtle.forward(35)
# right leg
turtle.left(45)
turtle.forward(45)
# back to body
turtle.right(180)
turtle.penup()
turtle.forward(45)
# left leg
turtle.pendown()
turtle.left(90)
turtle.forward(45)
# the end
turtle.done()
