nums = []

for i in range(5):
    n = int(input(f"Digite o {i + 1}º numero:"))
    nums.append(n)

menor = n

for n in nums:
    if menor > n:
        menor = n

maior = n

for n in nums:
    if maior < n:
        maior = n

print(f"Sua lista:{nums}")
print(f"Maior numero de sua lista:{maior}")
print(f"Menor numero de sua lista:{menor}")
