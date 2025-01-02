brasileirao = ("Corinthians", "Palmeiras", "Santos", "Gremio", "Cruzeiro", "Flamengo", "Vasco", "Chapecoense", "Atletico", "Botafogo", "Atletico-PR", "Bahia", "São Paulo", "Fluminense", "Sport Recife", "EC Vitoria", "Coritiba", "Avaí", "Ponte Preta", "Atletico-GO")

print("Os 5 primeiros colocados são: {}".format(brasileirao[:5]))

print("Os ultimos 4 colocados são: {}".format(brasileirao[-4:]))

print("Times em ordem alfabetica: {}".format(sorted(brasileirao)))

print("A Chapecoense está na {}ª posição".format(brasileirao.index("Chapecoense") + 1))
