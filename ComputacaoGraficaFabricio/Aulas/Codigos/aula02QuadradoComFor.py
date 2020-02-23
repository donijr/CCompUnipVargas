import turtle
lapis = turtle.Pen()

""" for i in range(4):   # desnhando quadrado simples
    lapis.forward(100)
    lapis.right(90)
input() """ 

# Desenhando dois quadrados separados
""" for i in range(4): 
    lapis.forward(100)
    lapis.right(90)

lapis.up() # levanta caneta
lapis.forward(200)
lapis.down() # abaixa caneta

for i in range(4):
    lapis.forward(100)
    lapis.right(90)
input() """

# Desenhando dois quadrados separados, cada um de uma cor
lapis.color("Red") # colocando cor na caneta
for i in range(4):
    lapis.forward(100)
    lapis.right(90)

lapis.up() # levanta caneta
lapis.forward(200)
lapis.down() # abaixa caneta

lapis.color("#808080") # colocando cor na caneta

for i in range(4):
    lapis.forward(100)
    lapis.right(90)
input()
