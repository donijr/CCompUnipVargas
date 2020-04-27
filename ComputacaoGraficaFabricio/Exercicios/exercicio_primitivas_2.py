import turtle

tartaruga = turtle.Turtle()
 
def desenha_quadrado(tamanho):
    for i in range (0,4):
        tartaruga.forward(tamanho)
        tartaruga.left(90)
        


def desenha_linha(tamanho,troca_cor):
    for i in range (0,8):
        tartaruga.down()
        if (troca_cor == True):
            if (i%2 == 0):
                tartaruga.fillcolor('white')
            else:
                tartaruga.fillcolor('black')
        else:
            if (i%2 != 0):
                tartaruga.fillcolor('white')
            else:
                tartaruga.fillcolor('black')
           
        tartaruga.begin_fill()
        desenha_quadrado(tamanho)
        tartaruga.end_fill()

        tartaruga.up()
        tartaruga.forward(tamanho)

def desenha_tabuleiro(tamanho):
    nova_posicao = posicao_inicial
    troca_cor = True

    for i in range(0,8):
        if (i%2 == 0): 
            troca_cor = True
        else:
            troca_cor = False

        desenha_linha(tamanho,troca_cor)
        nova_posicao = posicao_inicial + (0,tamanho*(i+1))
        tartaruga.setpos(nova_posicao)

tartaruga.speed(10)
posicao_inicial = tartaruga.pos()
desenha_tabuleiro(50)
input()
