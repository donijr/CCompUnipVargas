# 3 - Pintar um quadrado de verde e outro de vermelho. 


import turtle
import random
area_tela = turtle.Screen()
area_tela.setup(width=1280, height=720)

def desenha_quadrado(turtle):
    for i in range(4): 
        turtle.forward(50)
        turtle.right(90)




caneta = turtle.Turtle()
#Desenhando Primeiro quadrado
caneta.down()
caneta.fillcolor('green')
caneta.begin_fill()
desenha_quadrado(caneta)
caneta.end_fill()

caneta.up()
caneta.forward(100)

#Desenhando Segundo Quadrado
caneta.down()
caneta.fillcolor('red')
caneta.begin_fill()
desenha_quadrado(caneta)
caneta.end_fill()

input()