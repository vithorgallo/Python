numeros = []
quantidade = 0

for i in range(10):
    i = i + 1
    num = int(input(f"Digite o {i} numero:"))
    numeros.append(num)

num2 = int(input("Digite outro numero: "))
for num in numeros:
    if num2 == num:
     quantidade = quantidade + 1
if quantidade > 0:
   print(f"{num2} esta presente na lista")
   print(f"A quantidade que o numero {num2} aparece e: {quantidade}")
else:
   print(f"{num2} nao esta presente na lista")

 