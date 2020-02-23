import os

os.system("clear")
print("For em um String. String = Fabricio")
nome = "Fabricio" 
for letra in nome: # for percorre elementos na lista, no caso é uma string
    print(letra)

print("------------------------------------")
print("Primeiro for")
for i in range(10): # for com limitação de passos, desse modo i = 0 e vai até n-1, com incremento de +1
    print (i)

print("------------------------------------")
print("Segundo for")
for i in range(1,10,2): # for com limitacao de passos. for i in range (i=X, nº limite, incremento)
    print (i)