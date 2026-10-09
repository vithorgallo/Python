jogadores = []

for i in range(10):
    nome = input(f"Nome do jogador {i+1}: ")
    pontos = int(input(f"Pontos do jogador {nome}: "))
    jogadores.append((nome, pontos))

jogadores.sort(key=lambda x: x[1], reverse=True)

print("\n=== RANKING ===\n")

for i, jogador in enumerate(jogadores):
    nome = jogador[0]
    pontos = jogador[1]
    print(f"{i+1}º lugar: {nome} - {pontos} pontos")
