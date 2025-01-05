lista = []
continuar = "s"

while continuar == "s":

    valor = int(input("\nDigite um valor: "))

    if valor in lista:
        print("O valor informado ja está na lista, não irei colocar")
    else:
        lista.append(valor)

    continuar = input("Quer continuar? [S/N] ")

    if continuar == "n":
        break
    else:
        continue

lista.sort()
print(f"Voce digitou os valores {lista}")
