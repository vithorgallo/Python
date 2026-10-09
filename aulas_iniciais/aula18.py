import random

lista = []

for i in range(5):
    n = input(f"Digite o nome do {i + 1}º aluno:")
    lista.append(n)

random.shuffle(lista)

print(lista)