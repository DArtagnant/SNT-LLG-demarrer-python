from turtle import *


a = 5
x = 0
y = 0
for i in range(5):
    up()
    goto(x, y)
    down()
    circle(a)
    a += 20
    y -= 20

input()