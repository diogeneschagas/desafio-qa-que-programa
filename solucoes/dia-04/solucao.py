frase = input("digite uma frase: ")
contador = frase.split()
qtd_palavras = len(contador)
if (qtd_palavras == 1):
    print("O texto tem", qtd_palavras, " palavra")
elif (qtd_palavras == 0):
    print("nenhuma palavra encontrada!")
else:
    print("O texto tem", qtd_palavras, " palavras")