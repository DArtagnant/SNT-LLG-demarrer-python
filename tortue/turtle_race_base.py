#https://projects.raspberrypi.org/fr-FR/projects/turtle-race/

from turtle import *
from random import randint

speed(0)
penup()
hideturtle()
goto(-140, 140)

for etape in range(14) :
    write(etape, align= 'center')
    right(90)
    forward(10)
    pendown()
    forward(150)
    penup()
    backward(160)
    left(90)
    forward(20)

ada = Turtle()
ada.color('red')
ada.shape('turtle')
ada.penup()
ada.goto(-160, 100)
ada.pendown()

for tourner in range(100):
    ada.forward(randint(1, 5))

input()