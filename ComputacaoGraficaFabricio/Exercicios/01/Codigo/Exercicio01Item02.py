# 2- Pintar 2 quadrados em lugares aleatórios

import turtle
import random

def pos_aleatoria(turtle):
    x = random.randrange(-640,640)
    y = random.randrange(-360,360)
    turtle.setpos(x,y)
    return turtle.pos()

def desenha_quadrado(turtle):
    for i in range(4): 
        turtle.forward(50)
        turtle.right(90)

caneta = turtle.Turtle()
area_tela = turtle.Screen()
area_tela.setup(width=1280, height=720)

#Desenhando Primeiro quadrado
caneta.up()
pos_aleatoria(caneta)
caneta.down()
caneta.fillcolor('red')
caneta.begin_fill()
desenha_quadrado(caneta)
caneta.end_fill()

#Desenhando Segundo Quadrado
caneta.up()
pos_aleatoria(caneta)
caneta.down()
caneta.fillcolor('blue')
caneta.begin_fill()
desenha_quadrado(caneta)
caneta.end_fill()

input()