class pessoa:
    def __init__(self, n="None", i=0):
        self.nome = n
        self.idade = i

    def aniversario(self):
        self.idade = self.idade + 1

    def mostrar(self):
        return f"{self.nome} tem {self.idade} anos de idade."

    def __str__(self):
        return f"{self.nome} tem {self.idade} anos de idade."

    def __getstate__(self):
        return f"Estado: nome:{self.nome}; idade:{self.idade}"

pessoa1 = pessoa()