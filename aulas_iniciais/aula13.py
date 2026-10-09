time = []

while True:
    print("Opcao 1: Adicionar Jogador")
    print("Opcao 2: Ver Time")
    print("Opcao 3: Remover Jogador")
    print("Opcao 0: Sair")

    opcao = int(input("Digite a opcao:"))

    if opcao == 1:
        nome = input("Digite o nome do jogador:")
        time.append(nome)
        print("")

    elif opcao == 2:
        print("--- Time Atual ---")
        for pessoa in time:
            print(pessoa)

    elif opcao == 3:
        if len(time) == 0:
            print("A pilha esta vazia")
        else:
            removido = time.pop()
            print(f"{removido} foi removido do time")

    elif opcao == 0:
        break

    else:
        print("Opcao invalida")