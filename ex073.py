times = "Corinthians", "Palmeiras", "Santos", "Gremio", "Cruzeiro", "Flamengo", "Vasco", "Chapecoense", "Atletico-MG", "Botafogo", "Athletico-PR", "Bahia", "Sao Paulo", "Fluminense", "Sport", "Vitoria", "Coritiba", "Avai", "Ponte Preta", "Atletico-GO"

print("*" * 40)
print("Times do Brasileirao 2017:")
print(times)
print("*" * 40)
print("Os primeiros 5 times da tabela:")
print(times[0:5])
print("*" * 40)
print("Os ultimos 4 colocados:")
print(times[16:])
print("*" * 40)
print("Times em ordem alfabetica:")
print(sorted(times))
print("*" * 40)

print(f"A Chapecoense esta na {times.index("Chapecoense") + 1}ª posicao" )
