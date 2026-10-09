import os

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

limpar()

time = []
qntdJogador = int(input("Quantos jogadores tem no seu time:"))
limpar()

for i in range(qntdJogador):
    print(f"Jogador º{i+1}")
    nome = input("Nome do Jogador:")
    nome = nome.replace(" ", "").title()
    posicao = input("Posicao do Jogador:")
    posicao = posicao.replace(" ", "").title()
    idade = int(input("Idade do Jogador:"))
    camisa = int(input("Nº da Camisa:"))
    limpar()

    jogador = {
    'nome': nome,
    'posicao': posicao,
    'idade': idade,
    'camisa': camisa
    }

    time.append(jogador)

for i, jogador in enumerate(time, start=1):
   print(f"\n====== Jogador {i} ======")

for jogador in time:
    for chave, valor in jogador.items():
     print(f"{chave.capitalize()}: {valor}")


   