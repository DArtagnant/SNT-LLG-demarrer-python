import turtle

def saut(t, x, y):
    t.up()
    t.goto(x, y)
    t.down()

def eye(t, nbr, x, y):
    saut(t, x, y)
    rayon = 20
    for i in range(nbr):
        t.circle(rayon)
        rayon += 20

tortue = turtle.Turtle()
tortue.speed(0)
saut(tortue, 0, -150)
tortue.circle(300)
eye(tortue, 5, -150, 150)
eye(tortue, 5, 150, 150)
saut(tortue, 0, -75)
tortue.circle(50)
tortue.hideturtle()

input()