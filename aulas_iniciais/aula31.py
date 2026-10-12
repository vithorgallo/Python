def triangulo_retangulo():
    contador = 1
    base = int(input("Digite o valor da base:"))
    triangulo = ""
    while contador < base + 1:
        triangulo += "*" * contador + "\n"
        contador = contador + 1
    return triangulo

print(triangulo_retangulo())