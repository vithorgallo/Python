import os

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

limpar()

nome = input("Nome do Jogador:")
nome = nome.replace(" ", "").title()
posicao = input("Posicao do Jogador:")
posicao = posicao.replace(" ", "").title()
idade = int(input("Idade do Jogador:"))
camisa = int(input("Nº da Camisa:"))

jogador = {
    'nome': nome,
    'posicao': posicao,
    'idade': idade,
    'camisa': camisa
}

limpar()

print("Qual das informacoes voce deseja que seja mostrada?")
print("========================")
print("1 | Nome")
print("2 | Posicao")
print("3 | Idade")
print("4 | Camisa")
print("=======================")

procurado = input("O que deseja que seja mostrado:")
procurado = procurado.replace(" ", "").lower()

print(jogador.get(procurado))
