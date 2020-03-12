import turtle

caneta = turtle.Turtle()
area_desenho = turtle.Screen()
area_desenho.setup(width=800, height=600)
area_desenho.title("Exercício 02")

def sair():
    area_desenho.bye()


def triangulo():
    for i in range(3):
        caneta.forward(200)
        caneta.left(120)

area_desenho.listen()
caneta.up
caneta.setpos(-100,0)
caneta.down
caneta.fillcolor(1,0,0)
caneta.begin_fill()
triangulo()
caneta.up()
caneta.forward(200)
caneta.down()
triangulo()
caneta.end_fill()

area_desenho.onkeypress(sair,"A")
input()