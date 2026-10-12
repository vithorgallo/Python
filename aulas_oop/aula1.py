class pessoa:
    def __init__(self):
        self.nome = ""
        self.idade = 0

    def aniversario(self):
        self.idade = self.idade + 1

    def mostrar(self):
        return f"{self.nome} tem {self.idade} anos de idade."

pessoa_1 = pessoa()
pessoa_1.nome = input("Digite seu nome:")
pessoa_1.idade = int(input("Digite sua idade:"))
print(pessoa_1.mostrar())
pessoa_1.aniversario()
print(pessoa_1.mostrar())