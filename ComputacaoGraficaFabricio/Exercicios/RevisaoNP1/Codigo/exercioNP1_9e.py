import turtle

caneta = turtle.Turtle()

caneta.up()
caneta.setpos(0,350)

#Quadrado da Cabeça
caneta.down()
posicao_inicial = caneta.pos()
caneta.setheading(0)
caneta.forward(150)
caneta.setheading(270)
caneta.forward(150)
caneta.setheading(180)
caneta.forward(150)
caneta.setheading(90)
caneta.forward(150)

#Posicionar olho Esquerdo
caneta.up()
caneta.setheading(270)
caneta.forward(65)
caneta.setheading(0)
caneta.forward(45)

#Desenhar olho esquerdo
caneta.down()
caneta.circle(15)


#Posicionar olho Direito
caneta.up()
caneta.setheading(360)
caneta.forward(60)

#Desenhar olho Direito
caneta.down()
caneta.circle(15)

#posicionar nariz
caneta.up()
caneta.setheading(180)
caneta.forward(20)
caneta.setheading(270)
caneta.forward(30)

#desenhar Nariz
caneta.down()
caneta.setheading(120)
caneta.forward(20)
caneta.setheading(-120)
caneta.forward(20)
caneta.setheading(360)
caneta.forward(20)

#posicionar boca
caneta.up()
caneta.setheading(180)
caneta.forward(10)
caneta.setheading(270)
caneta.forward(20)
caneta.setheading(180)
caneta.forward(30)
caneta.setheading(0)

#desenhar boca
caneta.down()
caneta.forward(60)
caneta.setheading(270)
caneta.forward(15)
caneta.setheading(180)
caneta.forward(60)
caneta.setheading(90)
caneta.forward(15)

#posicionar corpo
caneta.up()
caneta.setpos(posicao_inicial)
caneta.setheading(270)
caneta.forward(150)
caneta.setheading(180)

#desenhar corpo
caneta.down()
caneta.forward(50)
caneta.setheading(270)
caneta.forward(300)
caneta.setheading(0)
caneta.forward(250)
caneta.setheading(90)
caneta.forward(300)
caneta.setheading(180)
caneta.forward(50)

#gravar posicao do corpo
caneta.up()
caneta.forward(200)
posicao_corpo = caneta.pos()

#posicionar perna esquerda
caneta.up()
caneta.setheading(270)
caneta.forward(300)
caneta.setheading(0)
caneta.forward(50)

#desenhar perna esquerda
caneta.down()
caneta.setheading(270)
caneta.forward(200)
caneta.setheading(0)
caneta.forward(50)
caneta.setheading(90)
caneta.forward(200)

#posicionar perna direita
caneta.up()
caneta.setheading(0)
caneta.forward(50)

#desenhar perna direita
caneta.down()
caneta.setheading(270)
caneta.forward(200)
caneta.setheading(0)
caneta.forward(50)
caneta.setheading(90)
caneta.forward(200)

#posicionar braço esquerdo
caneta.up()
caneta.setpos(posicao_corpo)

#desenhar braco esquerdo
caneta.down()
caneta.setheading(180)
caneta.forward(200)
caneta.setheading(270)
caneta.forward(50)
caneta.setheading(0)
caneta.forward(200)

#posicionar braco direito
caneta.up()
caneta.setheading(90)
caneta.forward(50)
caneta.setheading(0)
caneta.forward(250)

#desenhar braco direito
caneta.down()
caneta.forward(200)
caneta.setheading(270)
caneta.forward(50)
caneta.setheading(180)
caneta.forward(200)

""" #desenhar braço esquerdo
caneta.down()
caneta.forward(50)
caneta.setheading(270)
caneta.forward(400)
caneta.setheading(0)
caneta.forward(50)
#caneta.setheading() """



""" caneta.up()
caneta.forward(200)
caneta.down()
caneta.forward(50) """
input()