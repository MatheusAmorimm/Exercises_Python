jogador = {}
jogador["nome"] = str(input("Nome do Jogador: "))
partidas = int(input("Quantas partidas na carreira? "))
jogador["gols"] = []
total_gols = 0
for gol in range(0, partidas):
    gols_marcados = int(input(f"Quantos gols na partida {gol + 1}? "))
    total_gols += gols_marcados
    jogador["gols"].append(gols_marcados)

jogador["total"] = total_gols

print(jogador)
print("-#" * 30)
for chave, valor in jogador.items():
    print(f"{chave} tem o valor {valor}.")
print("-#" * 30)
print(f"O jogador {jogador["nome"]} jogou {partidas} partidas.")
for jogo, gols in enumerate(jogador["gols"]):
    print(f"{"=> Na partida ":>5}{jogo+1}{", fez "}{gols}{" gols"}")
print(f"Foi um total de {total_gols}")