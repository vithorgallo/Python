time = []

for i in range(5):
    print(f"--- Cadastro do jogador {i + 1} ---")

    nome = input("Nome: ")
    posicao = input("Posição: ")
    idade = int(input("Idade: "))

    jogador = {
        'nome': nome,
        'posição': posicao,
        'idade': idade
    }

    time.append(jogador)

print("===== TIME =====")

for jogador in time:
    print(f"Nome: {jogador['nome']}")
    print(f"Posição: {jogador['posição']}")
    print(f"Idade: {jogador['idade']}")
    print()

