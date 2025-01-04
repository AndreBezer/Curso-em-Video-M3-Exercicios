tupla = ("aprender", "vogal")
vogal = ("a", "e", "i", "o", "u")
vogais = []

#separa as palavras na tupla 
for contador in range(0 , len(tupla)):

#separa as vogais 
    for letra in tupla[contador]:
        if letra in vogal:
            vogais.append(letra)
    print(f"A palavra {tupla[contador]} possui {vogais} vogais",)
