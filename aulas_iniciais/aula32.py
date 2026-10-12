def triangulo():
    contador = 1
    base = int(input("Digite o valor da base:"))
    espaço = base
    triangulo = ""
    while contador < base + 1:
        triangulo += " " * espaço + "*" * contador + "\n"
        contador = contador + 2
        espaço = espaço - 1
    return triangulo

print(triangulo())