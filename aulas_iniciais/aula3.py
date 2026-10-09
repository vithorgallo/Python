print("--- Calculadora ---")

print("Opcao 1: Abrir")
print("Opcao 2: Sair")
opcao = int(input(""))

while opcao != 2:
    print("Digite o primeiro numero: ")
    num1 = float(input(""))
    print("Digite o segundo numero: ")
    num2 = float(input(""))

    print("Escolha a operacao: ")
    print("1: Soma (+)")
    print("2: Subtracao (-)")
    print("3: Multiplicacao (*)")
    print("4: Divisao (/)")

    resultado = 0

    operacao = int(input(""))
    if operacao == 1:
        resultado = num1 + num2
    elif operacao == 2:
        resultado = num1 - num2
    elif operacao == 3:
        resultado = num1 * num2
    else:
        resultado = num1 / num2
    print("")    

    print(f"O resultado e {resultado}")
    print("")


    print("Oque deseja fazer agora?")  
    print("Opcao 1: Continuar")
    print("Opcao 2: Sair")  
    opcao = int(input(""))