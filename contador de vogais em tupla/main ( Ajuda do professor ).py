tupla = ("aprender", "vogal")
vogal = ("a", "e", "i", "o", "u")
#vogais = []

#separa as palavras na tupla 
for contador in range(0 , len(tupla)):
    print("\nna palavra {} possui: ".format(tupla[contador]), end="")

#separa as vogais 
    for letra in tupla[contador]:
        if letra in vogal:
    
            print(f"{letra}", end=" ")
