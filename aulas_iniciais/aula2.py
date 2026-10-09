i = 0
soma = 0
numero = int(input("Digite um numero: "))

while numero != 0:
    i = i + 1
    soma += numero
    numero = int(input("Digite outro numero: "))

if i > 0:
    media = soma / i

print(f"O total de numeros diitados e:{i}")
print(f"A media dos numeros digitados e:{media}")