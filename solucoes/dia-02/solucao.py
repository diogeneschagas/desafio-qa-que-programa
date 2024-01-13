
x = float(input("informe um numero: "))
operacao = input("qual operacao (/ * + -): ")
y = float(input("informe outro numero: "))

if operacao == "/":
    if (y == 0):
        print("Não se pode dividir por zero!")
    else:
        resultado = x/y
        print(resultado)
elif operacao == "*":
    resultado = x*y
    print(resultado)
elif operacao == "+":
    resultado = x+y
    print(resultado)
elif operacao == "-":
    resultado = x-y
    print(resultado)
else:
    print("Operação inválida!")