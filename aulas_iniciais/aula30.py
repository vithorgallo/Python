import os

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

limpar()

def pedir_numero():
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    return n1, n2

def operacao():
    op = input("Digite a operação (símbolo): ")
    return op

def somar(n1, n2):
    resultado_soma = n1 + n2
    return resultado_soma

def multiplicar(n1, n2):
    resultado_mult = n1 * n2
    return resultado_mult

def dividir(n1, n2):
    resultado_div = n1 / n2
    return resultado_div

def subtrair(n1, n2):
    resultado_sub = n1 - n2
    return resultado_sub

def calcular():
    n1, n2 = pedir_numero()
    op = operacao()

    if op == "+":
        resultado_soma = somar(n1, n2)
        print("Resultado:", resultado_soma)

    if op == "-":
        resultado_sub = subtrair(n1, n2)
        print("Resultado:", resultado_sub)

    if op == "*":
            resultado_mult = multiplicar(n1, n2)
            print("Resultado:", resultado_mult)

    if op == "/":
            resultado_div = dividir(n1, n2)
            print("Resultado:", resultado_div)
    
calcular()
