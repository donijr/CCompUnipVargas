# 5- Fazer rotinas para figuras a serem utilizadas no desenho de uma casa
import turtle


caneta = turtle.Turtle()


# Funcao para desenha quadrado(parede) e triangulo equilatero(telhado)
def poligono_regular(n_lados, comp_lado, turtle):
    angulo_total = 360 / n_lados
    angulo_parcial = 360 / n_lados
    while (angulo_total <= 361):
        turtle.forward(comp_lado)
        turtle.setheading(angulo_total)
        angulo_total = angulo_total + angulo_parcial


# Funcao para desenha retangulo(porta)
def paralelogramo(angulo_1, angulo_2,base,altura,turtle):
    contador = 0
    angulo_total = 0
    while (contador < 4):
        if (contador % 2 == 0):
            angulo_total= angulo_total + angulo_2
            turtle.forward(base)
            turtle.setheading(angulo_total)
            contador = contador +1
        else:
            angulo_total= angulo_total + angulo_1
            turtle.forward(altura)
            turtle.setheading(angulo_total)
            contador= contador +1


# Desenhando Casa
poligono_regular(4, 100, caneta)
caneta.penup()
caneta.sety(100)
caneta.down()
poligono_regular(3,100,caneta)
caneta.up()
caneta.sety(0)
caneta.setx(35)
caneta.down()
paralelogramo(90,90,30,50,caneta)
input()