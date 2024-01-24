import time
print("""informe o tipo de contagem:
      1- progressiva
      2- regressiva
                      """)
tipo_contagem = input()

if (tipo_contagem != "1") and (tipo_contagem != "2"):
    print("selecione uma opção válida, seu animal! é entre 1 e 2!")
else:
    segundos = int(input("informe os segundos: "))

    if (tipo_contagem == "1"):
        contagem = 0
        final = segundos
        while (contagem < final):
            print(f"Contagem progressiva {contagem}")
            time.sleep(1)
            contagem += 1
        print("Fim da contagem!")

    elif (tipo_contagem == "2"):
        contagem = segundos
        final = 0
        while (contagem > final):
            print(f"Contagem regressiva {contagem}")
            time.sleep(1)
            contagem -= 1
        print("Fim da contagem!")

