import turtle

caneta = turtle.Turtle()

def desenha_cruz():
    origem = (0,0)

    caneta.up()
    caneta.setpos(origem)
    caneta.down()
    caneta.setheading(360)
    caneta.forward(200)
    caneta.up()
    caneta.setpos(origem)
    caneta.down()
    caneta.setheading(180)
    caneta.forward(200)
    caneta.up()
    caneta.setpos(origem)
    caneta.down()
    caneta.setheading(90)
    caneta.forward(200)
    caneta.up()
    caneta.setpos(origem)
    caneta.down()
    caneta.setheading(-90)
    caneta.forward(200)


caneta.fillcolor("grey")
caneta.begin_fill()
caneta.up()
caneta.setpos(0,0)
caneta.setpos(200,00)
caneta.down()
caneta.setpos(0,200)
caneta.setpos(-200,0)
caneta.setpos(0,-200)
caneta.setpos(200,00)
caneta.end_fill()
desenha_cruz()

input()