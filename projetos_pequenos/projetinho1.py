import os
import random

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def linha():
    print("=" * 50)

def espaço():
    print("")

def continuar():
    input("Pressione enter para continuar...")
    limpar()

def menu():
    linha()
    print("Menu")
    linha()
    print("1 - Atacar")
    print("2 - Curar")
    print("3 - Defender")
    linha()
    espaço()

def cadastrar_jogador():
    linha()
    print("CADASTRO", "=" * 40)
    linha()
    nome = input("Escolha seu nome: ")
    continuar()
    return nome

def mostrar_personagem(personagem):
    linha()
    print(personagem["nome"])
    linha()
    for chave, valor in personagem.items():
        print(f"{chave.capitalize()}: {valor}")
    linha()
    espaço()

def calcular_dano(atacante, defensor):
    ataque_do_atacante = atacante["ataque"]
    defesa_do_defensor = defensor["defesa"]
    dano = ataque_do_atacante - defesa_do_defensor
    if defensor["defendendo"]:
        dano = 0
    if dano < 1:
        dano = 1
    return dano

def turno_jogador(jogador, inimigo1):
    jogador["defendendo"] = False
    menu()

    while True:
        try:
            escolha = int(input("Escolha uma ação: "))

            if escolha in [1, 2, 3]:
                break

            print("Opção inválida, tente novamente.")
            continuar()
            menu()

        except ValueError:
            print("Digite apenas 1, 2 ou 3.")
            continuar()
            menu()

    if escolha == 1:
        dano = calcular_dano(jogador, inimigo1)
        inimigo1["vida"] -= dano

        print(
            f"{jogador['nome']} desferiu "
            f"{dano} de dano em {inimigo1['nome']}!"
        )

        continuar()

    elif escolha == 2:
        jogador["vida"] += 10

        if jogador["vida"] > jogador["vida_maxima"]:
            jogador["vida"] = jogador["vida_maxima"]

        print(f"{jogador['nome']} recuperou 10 pontos de vida!")

        continuar()

    elif escolha == 3:
        jogador["defendendo"] = True

        print(f"{jogador['nome']} está defendendo!")

        continuar()

def turno_inimigo(jogador, inimigo1):
    inimigo1["defendendo"] = False

    opcoes = [1, 2, 3]
    escolha = random.choice(opcoes)

    if escolha == 1:
        dano = calcular_dano(inimigo1, jogador)
        jogador["vida"] -= dano
        print(
            f"{inimigo1['nome']} desferiu "
            f"{dano} de dano em {jogador['nome']}!"
        )
        continuar()

    elif escolha == 2:
        inimigo1["vida"] += 10

        if inimigo1["vida"] > inimigo1["vida_maxima"]:
            inimigo1["vida"] = inimigo1["vida_maxima"]

        print(f"{inimigo1['nome']} recuperou 10 pontos de vida!")

        continuar()

    elif escolha == 3:
        inimigo1["defendendo"] = True
        print(f"{inimigo1['nome']} está defendendo!")
        continuar()

def verificar_vitoria(jogador, inimigo1):
    if jogador["vida"] <= 0:
        return True

    if inimigo1["vida"] <= 0:
        return True

    return False

def batalha(jogador, inimigo1):
    while not verificar_vitoria(jogador, inimigo1):
        mostrar_personagem(jogador)
        continuar()

        mostrar_personagem(inimigo1)
        continuar()

        turno_jogador(jogador, inimigo1)

        if verificar_vitoria(jogador, inimigo1):
            break

        turno_inimigo(jogador, inimigo1)
    limpar()

    linha()
    print("FIM DA BATALHA")
    linha()

    if jogador["vida"] <= 0:
        print(f"{jogador['nome']} foi derrotado!")
        print(f"{inimigo1['nome']} venceu!")

    elif inimigo1["vida"] <= 0:
        print(f"{inimigo1['nome']} foi derrotado!")
        print(f"{jogador['nome']} venceu!")
    linha()
    continuar()

limpar()
nome_jogador = cadastrar_jogador()

jogador = {
    "nome": nome_jogador,
    "vida": 50,
    "vida_maxima": 50,
    "ataque": 15,
    "defesa": 10,
    "defendendo": False
}

inimigo1 = {
    "nome": "Goblin",
    "vida": 70,
    "vida_maxima": 70,
    "ataque": 10,
    "defesa": 5,
    "defendendo": False
}

batalha(jogador, inimigo1)