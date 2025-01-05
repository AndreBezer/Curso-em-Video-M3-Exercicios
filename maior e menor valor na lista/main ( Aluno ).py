lista = []

for i in range(0, 5):
    lista.append(int(input("Digite um numero:")))

print(f"O maior valor encontrado na lista foi o numero: {max(lista)} na posição ", end="")
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
        print(f"{lista.index(i)} ", end="")
