import os

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def linha():
    print("="*30)

def pausa():
    input("\nPressione Enter para continuar...")

def pedirN():
    linha()
    n1 = int(input("Digite um número:"))
    linha()
    n2 = int(input("Digite outro número:"))
    linha()
    return n1, n2
    
def somar():
    n1, n2 = pedirN()
    s = n1 + n2
    print(f"Resultado:{s}")
    linha()
    pausa()
    limpar()

def subtrair():
    n1, n2 = pedirN()
    ss = n1 - n2
    print(f"Resultado:{ss}")
    linha()
    pausa()
    limpar()

def vezes():
    n1, n2 = pedirN()
    x = n1 * n2
    print(f"Resultado:{x}")
    linha()
    pausa()
    limpar()
    
def dividir():
    n1, n2 = pedirN()
    if n2 == 0:
            print("Tenta isso nao man")
            pausa()
            limpar()
    else:        
     d = n1 / n2
     print(f"Resultado:{d}")
     linha()
     pausa()
     limpar()

def menu():
    linha()
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("0 - Sair")
    linha()

limpar()
while True:
    menu()
    op = int(input("Digite a opção:"))
    limpar()
    if op == 1:
        somar()
    elif op == 2:
        subtrair()
    elif op == 3:
        vezes()
    elif op == 4:
        dividir()
    elif op == 0:
        break
    else:
        pausa()