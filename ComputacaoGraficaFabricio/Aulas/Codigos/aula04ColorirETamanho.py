import turtle

lapis = turtle.Turtle()


#Colorindo quadrado
lapis.fillcolor(1,0,0)

lapis.begin_fill()

for des in range (0,4):
    lapis.fd(200)
    lapis.right(90)

lapis.end_fill()

#mudando tamanho do lapis
lapis.pensize(10)
#mudando cor do lapis
lapis.pencolor(1,0.4,0) 
lapis.fd(100)


input()