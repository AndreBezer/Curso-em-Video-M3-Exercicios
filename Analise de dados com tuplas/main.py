lista = (int(input("Digite um numero: ")), int(input("Digite mais um numero: ")), int(input("Digite outro numero: ")), int(input("Digite o ultimo numero: ")))

print("\n", "-="*7)
print(f"Os numeros digitados foram {lista}")
print(f"O valor 9 aparaceu {lista.count(9)} vezes")

if 3 in lista:
    print(f"O numero 3 aparaceu na {lista.index(3) + 1} posição ")
else:
    print(f"O numero 3 não aparaceu nos valores digitados")

# Ajuda do professor: 

print("Os valores pares foram: ", end="")

for c in lista:
    if c % 2 == 0:
        print(c, end=" ")
