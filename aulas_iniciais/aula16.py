dados = []

qntd = int(input("Digite a quantidade de pessoas:"))

for i in range(qntd):
    i = i + 1
    nome = input(f"Digite o nome da {i}º pessoa:")
    idade = int(input(f"Digite a idade de {nome}:"))
    cidade = input(f"Digite a cidade de {nome}:")
    dados.append(((nome, idade, cidade)))

print("")

for a in range(qntd):
    print(f"Dados da {a + 1}º pessoa:")
    print(dados[a])