produtos = []
qntd = int(input("Digite a quantidade de produtos que voce deseja cadastrar:"))

for i in range(qntd):
    nome = str(input("Digite o nome do produto:"))
    preco = float(input(f"Digite o preco do produto {nome}:"))

