import turtle

tartaruga1 = turtle.Turtle()
tartaruga2 = turtle.Turtle()

tartaruga1.pencolor(1,0,0)
tartaruga2.pencolor(0,0,1)

posicao_inicial_t1 = (0,0)
posicao_inicial_t2 = (100,100)

tartaruga1.up()
tartaruga2.up()

tartaruga1.setposition(posicao_inicial_t1)
tartaruga2.setposition(posicao_inicial_t2)

tartaruga1.left(90)
tartaruga2.right(90)

tartaruga1.down()
tartaruga2.down()

tartaruga1.forward(100)
tartaruga2.forward(100)

tartaruga1.left(-90)
tartaruga2.right(90)

tartaruga1.forward(100)
tartaruga2.forward(100)

input()