# 1- Fazer um programa para desenhar um quadrado de lado 50 em um lugar aleatório da tela
import turtle
import random

caneta = turtle.Turtle()
area_tela = turtle.Screen()
area_tela.setup(width=1280, height=720)

x = random.randrange(-640,640)
y = random.randrange(-360,360)

caneta.up()
caneta.setpos(x,y)
caneta.down()

for i in range(4): 
    caneta.forward(50)
    caneta.right(90)

input()