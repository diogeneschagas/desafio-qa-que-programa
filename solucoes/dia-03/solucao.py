palavra_certa = input("informe palavra/frase para checagem de palíndromo: ").lower()
sem_espacos = palavra_certa.replace(' ', '')
formatado = sem_espacos.replace('.', '')
formatado = sem_espacos.replace('?', '')
formatado = sem_espacos.replace('!', '')
formatado = sem_espacos.replace(',', '')


txt_invertido = ""
for caractere in formatado:
    txt_invertido = caractere + txt_invertido

if formatado == txt_invertido:
    resultado = "este txt é um palíndromo"
else:
    resultado = "este txt NÃO é um palíndromo"

print(resultado)