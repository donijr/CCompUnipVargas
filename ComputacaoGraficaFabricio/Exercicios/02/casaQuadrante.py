# Criar um elemento gráfico (Exemplo casa) onde fique nos 4 quadrantes da tela.


import turtle

lapis = turtle.Turtle()

def desenha_casa():
    posicao_inicial = lapis.pos()
    lapis.setheading(180)
    lapis.forward(100)
    lapis.setheading(60)
    lapis.forward(100)
    lapis.setheading(-60)
    lapis.forward(100)
    lapis.setheading(-90)
    lapis.forward(100)
    lapis.setheading(180)
    lapis.forward(100)
    lapis.setheading(90)
    lapis.forward(100)

    lapis.up()
    lapis.setposition(posicao_inicial + (-65,-100))
    lapis
    lapis.down()
    lapis.forward(50)
    lapis.right(90)
    lapis.forward(30)
    lapis.right(90)
    lapis.forward(50)

def desenha_quadrantes():
    lapis.up()
    lapis.setpos(0,0)
    lapis.down()
    lapis.setx(640)
    lapis.up()
    lapis.setpos(0,0)
    lapis.down()
    lapis.setx(-640)
    lapis.up()
    lapis.setpos(0,0)
    lapis.down()
    lapis.sety(340)
    lapis.up()
    lapis.setpos(0,0)
    lapis.down()
    lapis.sety(-340)

desenha_quadrantes()
#quadrante superior esquerdo
lapis.up()
lapis.setpos(-350,200)
lapis.pendown()
desenha_casa()

#quadrante superior direito
lapis.up()
lapis.setpos(350,200)
lapis.pendown()
desenha_casa()

#quadrante inferior esquerdo
lapis.up()
lapis.setpos(-350,-200)
lapis.pendown()
desenha_casa()

#quadrante inferior direito
lapis.up()
lapis.setpos(350,-200)
lapis.pendown()
desenha_casa()

input()
