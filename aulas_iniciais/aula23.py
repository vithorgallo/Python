def imprimir_tabuleiro(tabuleiro):
    print("\n")
    print(f" {tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]} ")
    print("---|---|---")
    print(f" {tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]} ")
    print("---|---|---")
    print(f" {tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]} ")
    print("\n")

def verificar_vitoria(tab, jog):
    condicoes = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], 
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]             
    ]
    return any(all(tab[pos] == jog for pos in linha) for linha in condicoes)

def jogar():
    tabuleiro = [str(i) for i in range(1, 10)]
    jogador_atual = "X"
    jogadas = 0

    print("--- JOGO DA VELHA ---")
    print("Escolha uma posição de 1 a 9 para jogar.")

    while jogadas < 9:
        imprimir_tabuleiro(tabuleiro)
        
        try:
            escolha = int(input(f"Jogador [{jogador_atual}], escolha sua posição: ")) - 1
            
            if escolha < 0 or escolha > 8 or tabuleiro[escolha] in ["X", "O"]:
                print("Posição inválida ou já ocupada! Tente novamente.")
                continue
                
        except ValueError:
            print("Digite um número válido entre 1 e 9!")
            continue

        tabuleiro[escolha] = jogador_atual
        jogadas += 1

        if verificar_vitoria(tabuleiro, jogador_atual):
            imprimir_tabuleiro(tabuleiro)
            print(f" Parabéns! O jogador [{jogador_atual}] venceu!")
            return

        jogador_atual = "O" if jogador_atual == "X" else "X"

    imprimir_tabuleiro(tabuleiro)
    print(" Deu velha! Empate.")

if __name__ == "__main__":
    jogar()


        



        
