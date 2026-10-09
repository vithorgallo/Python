alunos = []
qntdAlunos = int(input("Digite a quantidade de alunos: "))

for i in range(qntdAlunos):
    aluno = str(input("Digite o nome do aluno:"))
    nota = float(input(f"Digite a nota do aluno {aluno}: "))
    alunos.append((aluno, nota))

melhorNota = nota
melhorAluno = aluno
piorNota = nota
piorAluno = aluno

if melhorNota < nota:
   melhorNota = nota
   melhorAluno = aluno

if piorNota > nota:
   piorNota = nota
   piorAluno = aluno

for aluno, nota in alunos:
    if nota >= 6:
     print(f"{aluno}: Aprovado")

print(f"O melhor aluno e: {melhorAluno} com a nota: {melhorNota}")
print(f"O pior aluno e: {piorAluno} com a nota: {piorNota}")
