import turtle

caneta = turtle.Turtle()


def quadrado():
    for i in range (4):
        caneta.left(90)
        caneta.forward(100)

caneta.right(20)
quadrado()
caneta.right(20)
quadrado()
caneta.right(20)
quadrado()


input()