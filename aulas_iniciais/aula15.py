banco = []

while True:
    print("Op 1: Adicionar Cliente a fila:")
    print("Op 2: Ver fila atual:")
    print("Op 3: Atender o primeiro Cliente:")
    print("Op 0: Sair")

    op = int(input("Selecione a opcao:"))

    if op == 1:
        cliente = input("Nome do cliente:")
        print(f"Cliente {cliente} cadastrado:")
        banco.append(cliente)

    elif op == 2:
        if len(banco) == 0:
            print("Nao ha clientes")
        else:
            for cliente in banco:
                print(f"Fila atual {cliente}")

    elif op == 3:
         if len(banco) == 0:
            print("Nao ha clientes")
         clienteAtendido = banco.pop(0)
         print(f"cliente {clienteAtendido} foi atendido")

    elif op == 0:
        break

    else:
        print("OP INVALIDA!!!")

    