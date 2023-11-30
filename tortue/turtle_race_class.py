#https://projects.raspberrypi.org/fr-FR/projects/turtle-race/

import turtle as t
from random import randint

class Coureur(t.Turtle):
    def __init__(self, color, x, y, *_, full_circle= False) -> None:
        super().__init__(shape= 'turtle', visible= True)
        self.color(color)
        self.penup()
        self.goto(x, y)
        self.pendown()
        if full_circle:
            self.full_circle()
    
    def full_circle(self):
        for _ in range(10):
            self.right(36)

    def random_forward(self) -> None:
        self.forward(randint(0, 5))

def write_terrain(turtle: t.Turtle, nbr_etape):
    turtle.hideturtle()
    turtle.speed(0)
    turtle.penup()
    turtle.goto(-140, 140)
    
    for etape in range(nbr_etape):
        turtle.write(etape, align= 'center')
        turtle.right(90)
        turtle.forward(10)
        for _ in range(8):
            turtle.pendown()
            turtle.forward(10)
            turtle.penup()
            turtle.forward(10)
        turtle.backward(170)
        turtle.left(90)
        turtle.forward(20)

write_terrain(t.Turtle(), 14)
colors = ['blue', 'green', 'red', 'orange']
turtles = [Coureur(c, -160, 100 - (25 * n), full_circle= True) for n, c in enumerate(colors)]
for tourner in range(100):
    for turtle in turtles:
        turtle.random_forward()

input()