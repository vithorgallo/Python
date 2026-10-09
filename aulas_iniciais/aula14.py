biblioteca = []

while True:
    print("Op 1: Adicionar livro")
    print("Op 2: Ver biblioteca")
    print("Op 3: Remover livro")
    print("Op 0: Sair")

    opcao = int(input("Selecione a opcao:"))

    if opcao == 1:
        livro = input("Nome do livro:")
        biblioteca.append(livro)

    elif opcao == 2:
        if len(biblioteca) == 0:
            print("Biblioteca Vazia")
        else:
         print("Biblioteca atual:")
         for livro in biblioteca:
            print(livro)

    elif opcao == 3:
        if len(biblioteca) == 0:
            print("Biblioteca Vazia")
        else:
            rLivro = biblioteca.pop()
            print(f"{rLivro} foi removido")

    elif opcao == 0:
        break

    else:
        print("Opcao invalida")
