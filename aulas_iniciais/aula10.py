alunos = []
qntd = int(input("Total de alunos na sala de aula:"))
soma = 0

for i in range(qntd):
    nome = str(input("Nome do aluno:"))
    nota = float(input(f"Nota do aluno {nome}:"))

alunos.append((nome, nota))
soma += nota

melhorNota = nota
melhorAluno = nome
piorNota = nota
piorAluno = nome

if melhorNota < nota:
   melhorNota = nota
   melhorAluno = nome

if piorNota > nota:
   piorNota = nota
   piorAluno = nome


qntdReprovados = 0
qntdAprovados = 0
aprovados = []
reprovados = []

for nome, nota in alunos:
    if nota >= 6:
      alunos.append((nome, nota))
      aprovados.append(nome)
      qntdAprovados = qntdAprovados + 1

for nome, nota in alunos:
    if nota < 6:
        alunos.append((nome, nota))
        reprovados.append(nome)
        qntdReprovados = qntdReprovados + 1

media = soma / qntd

print(alunos)
print(piorAluno)
print(melhorAluno)
print(media)
print(aprovados)
print(reprovados)
print(qntdAprovados)
print(qntdReprovados)

     


