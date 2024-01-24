import random

lista_numeros = []
while (len(lista_numeros) < 6):
    numero = random.randrange(1, 61)
    lista_numeros.append(numero)

print(lista_numeros)