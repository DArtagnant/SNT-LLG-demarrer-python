from turtle import *

def saut(x, y):
    penup()
    goto(x, y)
    pendown()

def rectangle(long, larg):
    for _ in range(2):
        forward(long)
        left(90)
        forward(larg)
        left(90)


rectangle(100, 80)
saut(20, 0)
rectangle(20, 40)
saut(70, 50)
circle(10)
saut(0, 80)
goto(50, 130)
goto(100, 80)
saut(0, 0)


input()