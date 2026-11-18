print("Escolha a operação:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

resposta = "s"

while resposta == "s":
    opcao = input("Digite o número da operação desejada: ")
    num1 = float(input("Digite o primeiro número da equação: "))
    num2 = float(input("Digite o segundo numero da equação: "))

    if opcao == "1":
        resultado = num1 + num2
        print(resultado)
    elif opcao == "2":
        resultado = num1 - num2
        print(resultado)
    elif opcao == "3":
        resultado = num1 * num2
        print(resultado)
    elif opcao == "4":
        if num1 == 0:
            print("Erro: o denominador tem que ser diferente de 0")
        else:
            resultado = num1 / num2
            print(resultado)
    else:
        print("Operação inválida, selecione um número de 1 a 4")

    resposta = input("Continuar as operações? ")
    
print("Operações Finalizadas")