import turtle

lapis = turtle.Turtle()

def casa_escala(n):
    lapis.forward(n*100)
    lapis.left(120)
    lapis.forward(n*100)
    lapis.left(120)
    lapis.forward(n*100)
    lapis.left(30)
    lapis.forward(n*100)
    lapis.left(90)
    lapis.forward(n*100)
    lapis.left(90)
    lapis.forward(n*100)

    lapis.up()
    lapis.setposition(n*35,n*-100)
    lapis.down()
    lapis.forward(n*50)
    lapis.right(90)
    lapis.forward(n*30)
    lapis.right(90)
    lapis.forward(n*50)

casa_escala(2)

input()