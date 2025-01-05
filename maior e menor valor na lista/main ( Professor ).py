lista = []
maior = 0
menor = 0

for i in range(0, 5):
    lista.append(int(input("Digite um numero:")))

    if i == 0:
        maior = menor = lista[i]

    else:
        if lista[i] > maior:
            maior = lista[i]
        
        if lista[i] < menor:
            menor = lista[i]
    
print(f"O maior valor encontrado foi {maior} na posição ", end="")
for i, v in enumerate(lista):
    if v == maior:
        print(f"{i}, ", end="")

print(f"\nO menor valor encontrado foi {menor} na posição ", end="")
for i, v in enumerate(lista):
    if v == menor:
        print(f"{i}, ", end="")

"""print(f"O maior valor encontrado na lista foi o numero: {max(lista)} na posição ", end="")
for i in lista:
    # se o valor for igual ao minimo
    if i == max(lista):
        # imprima o index do valor
        print(f"{lista.index(i)} ", end="")

print(f"\nO menor valor encontrado na lista foi o numero: {min(lista)} na posição ", end="")

#para cada valor na lista
for i in lista:
    # se o valor for igual ao minimo
    if i == min(lista):
        # imprima o index do valor
        print(f"{lista.index(i)} ", end="")"""
