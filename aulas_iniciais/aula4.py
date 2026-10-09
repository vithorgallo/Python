numeros = []
soma = 0
totalNum = 0
qntdRange = int(input("Digite o tamanho a sua lista: "))

for i in range(qntdRange):
    num = int(input("Digite um numero: "))
    numeros.append(num)
    soma += num


maior = numeros[0]
menor = numeros[0]

pares = []
for num  in numeros:
        if num % 2 == 0:
         pares.append(num)

impares = []
for num  in numeros:
        if num % 2 != 0:
         impares.append(num)

for num in numeros:
    if num > maior:
        maior = num
    if num < menor:
        menor = num

media = soma / (qntdRange)

print("")
print("====================================")
print("--- DADOS DA LISTA ---")
print("====================================")
print("")
print(f"Numeros digitados: {numeros}")
print(f"Os numeros pares sao: {pares}")
print(f"Os numeros impares sao: {impares}")
print(f"Maior numero: {maior}")
print(f"Menor numero: {menor}")
print(f"Soma dos Numeros: {soma}")
print(f"A media dos Numeros: {media}")
print(f"O total de Numeros digitados e: {qntdRange}")