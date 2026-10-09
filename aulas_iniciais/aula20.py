cont = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')

while True:
    num = int(input("Digite um numero entre 0 e 10:"))
    if 0 <= num <= 20:
        break
    print("Numero errado, pense direito:")
print(f'Voce digitou o numero {cont[num]}')