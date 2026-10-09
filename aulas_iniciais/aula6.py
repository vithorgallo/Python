pontuacao = []

for i in range(10):
    i = i + 1
    pontos = int(input(f"Digite a pontuaçao do jogador {i}: "))
    pontuacao.append(pontos)

primeiro = segundo = terceiro = quarto = quinto = sexto = setimo = oitavo = nono = ultimo = float("-inf")

for pontos in pontuacao:
    if pontos > primeiro:
        ultimo = nono
        nono = oitavo
        oitavo = setimo
        setimo = sexto
        sexto = quinto
        quinto = quarto
        quarto = terceiro
        terceiro = segundo
        segundo = primeiro
        primeiro = pontos

    elif pontos > segundo:
        ultimo = nono
        nono = oitavo
        oitavo = setimo
        setimo = sexto
        sexto = quinto
        quinto = quarto
        quarto = terceiro
        terceiro = segundo
        segundo = pontos

    elif pontos > terceiro:
        ultimo = nono
        nono = oitavo
        oitavo = setimo
        setimo = sexto
        sexto = quinto
        quinto = quarto
        quarto = terceiro
        terceiro = pontos

    elif pontos > quarto:
        ultimo = nono
        nono = oitavo
        oitavo = setimo
        setimo = sexto
        sexto = quinto
        quinto = quarto
        quarto = pontos

    elif pontos > quinto:
        ultimo = nono
        nono = oitavo   
        oitavo = setimo
        setimo = sexto
        sexto = quinto
        quinto = pontos
        
    elif pontos > sexto:
        ultimo = nono
        nono = oitavo
        oitavo = setimo
        setimo = sexto
        sexto = pontos

    elif pontos > setimo:
        ultimo = nono
        nono = oitavo
        oitavo = setimo
        setimo = pontos

    elif pontos > oitavo:
        ultimo = nono
        nono = oitavo  
        oitavo = pontos

    elif pontos > nono:
        ultimo = nono
        nono = pontos

    elif pontos > ultimo:
        ultimo = pontos 

print("")
print("===============================")
print("--- RANKING DE PONTUACAO ---")
print("===============================")
print("")
print("===============================")
print(f"Primeiro Lugar: #{primeiro} pontos")
print("===============================")
print(f"Segundo Lugar: #{segundo} pontos")
print("===============================")
print(f"Terceiro Lugar: #{terceiro} pontos")
print("===============================")
print(f"Quarto Lugar: #{quarto} pontos")
print("===============================")
print(f"Quinto Lugar: #{quinto} pontos")
print("===============================")
print(f"Sexto Lugar: {sexto} pontos")
print("===============================")
print(f"Setimo Lugar: #{setimo} pontos")
print("===============================")
print(f"Oitavo Lugar: #{oitavo} pontos")
print("===============================")
print(f"Nono Lugar: #{nono} pontos")
print("===============================")
print(f"Ultimo Lugar: #{ultimo} pontos")
print("===============================")