import os

def limpar():
    os.system("cls" if os.name == "nt" else "clear")
def pausar():
    input("\nPressione Enter para continuar...")

limpar()

matriz = []

linhas = 3
colunas = 3

for i in range(linhas):

    linha = []

    for j in range(colunas):

        numero = int(input(f"Digite o valor para [{i}][{j}]: "))
        linha.append(numero)

    matriz.append(linha)

limpar()

while True:
 print("===========================")
 for linha in matriz:
    print(linha)
 print("===========================")
 print("1 - Maior Numero")
 print("2 - Menor Numero")
 print("3 - Soma Total")
 print("4 - Numeros Pares")
 print("5 - Numeros Impares")
 print("6 - Somas Diagonais")
 print("7 - Busca Linear")
 print("0 - Sair")
 print("===========================")

 try:
      op = int(input("Selecione a opção:"))
 except ValueError:
      print("Opçao invalida")
      pausar()
      continue
 
 if op == 1:
        maior = matriz[0][0]
         
        for linha in matriz:
            for numero in linha:
                if maior < numero:
                    maior = numero
                    
        print(f"Numero Maior: {maior}")
        pausar()
        limpar()

 elif op == 2:         
        menor = matriz[0][0]

        for linha in matriz:
            for numero in linha:
                if menor > numero:
                    menor = numero

        print(f"Numero Menor: {menor}")
        pausar()
        limpar()

 elif op == 3:
        soma = 0

        for linha in matriz:
            for numero in linha:
                soma += numero

        print(f"Soma total é: {soma}")
        pausar()
        limpar()

 elif op == 4:
  pares = []

  for linha in matriz:
    for numero in linha:
        if numero % 2 == 0:
            pares.append(numero)

  print(f"Numeros pares: {pares}")
  pausar()
  limpar()
    
 elif op == 5:
  impares = []

  for linha in matriz:
    for numero in linha:
        if numero % 2 != 0:
            impares.append(numero)

  print(f"Numeros impares: {impares}")
  pausar()
  limpar()
 
 elif op == 6:
    print("=======================")
    print("1 - Diagonal (dir-cima) -> (esq-baixo)")
    print("2 - Diagonal (esq-cima) -> (dir-baixo)")

    try:
     op2 = int(input("Selecione qual diagonal:"))
    except ValueError:
     print("Opção Invalida")
     pausar()
     continue

    if op2 == 1:
     print("Diagonal 1:")
     print(f"{matriz[0][0]}[][]")
     print(f"[]{matriz[1][1]}[]") 
     print(f"[][]{matriz[2][2]}")       
     pausar()
     limpar()

    elif op2 == 2:
     print("Diagonal 2:")
     print(f"[][]{matriz[0][2]}")
     print(f"[]{matriz[1][1]}[]")
     print(f"{matriz[2][0]}[][]")       
     pausar()
     limpar()


 elif op == 7:
    try:
        procurado = int(input("Procure um número na Matriz: "))
    except ValueError:
        print("Por favor, digite um número inteiro válido.")
        pausar()
        limpar()
        continue

    encontrado = False
    posicao = ""

    for i in range(linhas):
        for j in range(colunas):
            if matriz[i][j] == procurado:
                encontrado = True
                posicao = f"[{i}][{j}]"
                break
        if encontrado:
            break

    if encontrado:
        print(f"\nO número {procurado} foi encontrado na posição {posicao}!")
    else:
        print(f"\nO número {procurado} não foi encontrado na matriz.")

    pausar()
    limpar()

 elif op == 0:
     break
