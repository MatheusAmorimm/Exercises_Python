from time import sleep

jogador = {}
jogadores = []
while True:
    jogador.clear()
    jogador["nome"] = str(input("Nome do Jogador: "))
    partidas = int(input("Quantas partidas na carreira? "))
    jogador["gols"] = []
    total_gols = 0
    for gol in range(0, partidas):
        gols_marcados = int(input(f"Quantos gols na partida {gol + 1}? "))
        total_gols += gols_marcados
        jogador["gols"].append(gols_marcados)
    jogador["total"] = total_gols
    jogadores.append(jogador.copy())
    resposta = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    while resposta != "S" and resposta != "N":
        resposta = str(input("Tente novamete. Quer continuar? [S/N] ")).strip().upper()[0]
    if resposta == "N":
        break

print("-" * 40)
print("cod ", end="")
for item in jogador.keys():
    print(f"{item:<15}", end="")
print()
print("-" * 40)
for indice, jog in enumerate(jogadores):
    print(f"{indice:>3} ", end="")
    for dado in jog.values():
        print(f"{str(dado):<15}", end="")
    print()
while True:
    print("-" * 30)
    relatorio = int(input("Deseja ver o relatorio de qual jogador? (Digite o codigo do jogador) (999 encerra)"))

    if relatorio == 999:
        break
    while relatorio < 0 or relatorio >= len(jogadores):
        print("[ERRO] - Codigo invalido!")
        relatorio = int(input("Digite o codigo do jogador que quer ver: "))

    if relatorio <= len(jogadores) - 1:
        print(f"-- Relatorio de gols do jogador {jogadores[relatorio]['nome']}")
        for jogo, gols in enumerate(jogadores[relatorio]["gols"]):
            print(f"=> Na partida {jogo + 1}, fez {gols} gols")

print("finalizando...")
sleep(1)
print("-" * 30)
print("Volte sempre!")
