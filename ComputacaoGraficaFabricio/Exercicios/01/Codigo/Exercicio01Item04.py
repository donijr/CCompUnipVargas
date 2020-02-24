# 4 - Fazer uma rotina para desenhar quadrados

import turtle
import random


def desenha_quadrado(turtle):
    for i in range(4): 
        turtle.forward(50)
        turtle.right(90)

caneta = turtle.Turtle()

desenha_quadrado(caneta)



input()