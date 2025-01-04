lista = ("Lápis", "Boarracha", "Caderno", "Estojo", "Transferidor", "Compasso", "Mochila", "Caneta", "Livro")

preco = ("1.75", "2.00", "15.90",  "25.00", "4,20", "9.99", "120.30", "22.30", "34.90")

for cont in range(0, len(lista)):
    print(f"{lista[cont]} --- {preco[cont]}")
