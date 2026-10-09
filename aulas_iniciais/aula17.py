dados = []
for i in range(5):
    nome = str(input(f"Digite o nome da {i + 1}º pessoa: "))
    idade = int(input(f"Digite a idade de {nome}: "))
    cidade = input(f"Digite a cidade de {nome}: ")


    dados.append((nome, idade, cidade))
print()

procurado = str(input("Digite o nome de quem você deseja procurar: "))

encontrado = False

for nome, idade, cidade in dados:
    if procurado == nome:
        encontrado = True
        print("\nPessoa encontrada!")
        print(f"Nome: {nome}")
        print(f"Idade: {idade}")
        print(f"Cidade: {cidade}")
        break


if not encontrado:
    print(f"{procurado} não está no sistema")













