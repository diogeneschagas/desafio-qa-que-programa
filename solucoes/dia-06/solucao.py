medidas = ["Quilômetros", "Milhas", "Metros", "Pés", "Graus Celsius", "Fahrenheint"]

print(""" 
    Selecione uma opção a seguir:
      0 - Quilômetros --> milhas
      1 - Milhas --> Quilômetros
      2 - Metros --> Pés
      3 - Pés --> Metros
      4 - Graus Celsius --> Farenheint 
      5 - Farenheint --> Graus Celsius
""")

entrada1 = input("selecione uma opção: ")
entrada2 = int(input("Informe o valor que você deseja converter: "))

if (entrada1 == "0"):
    resultado = entrada2 * 0.621371
else:
    if (entrada1 == "1"):
        resultado = entrada2 * 1.60934
    elif (entrada1 == "2"):
        resultado = entrada2 * 3.28084
    elif (entrada1 == "3"):
        resultado = entrada2 * 0.3048
    elif (entrada1 == "4"):
        resultado = entrada2 * 33.8
    elif (entrada1 == "5"):
        resultado = (entrada2 - 32) * 5/9
    else:
        print("insira uma opção válida")
        resultado = 0
print(resultado)