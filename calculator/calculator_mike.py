# Console Calculator made using python.

def sum(x, y):
    return x + y

def subtract(x, y):
    return x - y

def divide(x, y):
    return x / y

def multiply(x, y):
    return x * y

isActive = True # Is this program being used at the moment? If not, stop the loop.

while (isActive):
    print("Bem vindo a calculadora python.")
    print("Escolha uma das opcoes: ")
    print("1-Soma | 2-Subtracao | 3-Multiplicacao | 4-Divisao | q-Sair.")
    opt = input("Opção: ")
    if opt == "1":
        inputx = float(input("Informe o primeiro valor: "))
        inputy = float(input("Informe o segundo valor: "))
        output = sum(inputx, inputy)
        print("Resultado = " + str(output))
        print()
    elif opt == "2":
        inputx = float(input("Informe o primeiro valor: "))
        inputy = float(input("Informe o segundo valor: "))
        output = subtract(inputx, inputy)
        print("Resultado = " + str(output))
        print()
    elif opt == "3":
        inputx = float(input("Informe o primeiro valor: "))
        inputy = float(input("Informe o segundo valor: "))
        output = multiply(inputx, inputy)
        print("Resultado = " + str(output))
        print()
    elif opt == "4":
        inputx = float(input("Informe o primeiro valor: "))
        inputy = float(input("Informe o segundo valor: "))
        output = divide(inputx, inputy)
        print("Resultado = " + str(output))
        print()
    elif opt == "q":
        print()
        print("Obrigado! Até logo.")
        isActive = False
    else:
        print("Opção inválida.")
        print()
    
