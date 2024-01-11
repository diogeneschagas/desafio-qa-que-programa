entrada = input("Informe o número desejado: ")

if entrada.isdigit():
    entrada_num = int(entrada)
    checagem_par_impar = entrada_num % 2

    if entrada == 0:
        print("zero não é divisível por nenhum número")
    elif checagem_par_impar == 0:
        print("este número é par")
    elif checagem_par_impar != 0:
        print("este é ímpar")

else:
    print("Por favor, informe um número válido.")