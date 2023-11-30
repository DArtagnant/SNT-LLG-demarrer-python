import turtle

def triangle(t: turtle.Turtle, taille_cote):
    for _ in range(3):
        t.forward(taille_cote)
        t.left(120)

def multi_triangles(t: turtle.Turtle, nbr):
    for n in range(nbr):
        triangle(t, 20 + (20 * n))
        t.up()
        t.right(90)
        t.forward(7)
        t.right(90)
        t.forward(10)
        t.right(180)
        t.down()

tortue = turtle.Turtle()
tortue.speed(0)
multi_triangles(tortue, 5)


input()