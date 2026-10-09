numeros = []

for i in range(10):
    num = int(input("Digite seu numero: "))
    numeros.append(num)

pares = []
for num  in numeros:
        if num % 2 == 0:
         pares.append(num)

impares = []
for num  in numeros:
        if num % 2 != 0:
         impares.append(num)
        
print(pares)
print(impares)


        
