def form(name="<desconhecido>", gols=0):
    if name == "" and gols == "":
        name = "<desconhecido>"
        gols = 0
    elif name == "":
        name = "<desconhecido>"
    elif gols == "":
        gols = 0
    return f"O jogador {name} fez {gols} gol(s) no campeonato"

atlhete = str(input("Digite o nome do jogador: "))
gol = str(input("Digite a quantidade de gols: "))
if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0

print(form(atlhete, gol))