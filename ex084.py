pessoas = []
dados = []
maiorPeso = 0
menorPeso = 0
while True:
    dados.append(str(input("Nome: ")))
    dados.append(float(input("Peso: ")))
    if len(pessoas) == 0:
       maiorPeso = menorPeso = dados[1]
    else:
        if dados[1] > maiorPeso:
            maiorPeso = dados[1]
        if dados[1] < menorPeso:
            menorPeso = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    resposta = str(input("Deseja cadastrar uma nova pessoa? [S/N] ")).strip().upper()
    while resposta != "S" and resposta != "N":
        resposta = str(input("Tente Novamente. Deseja cadastrar uma nova pessoa? [S/N]")).strip().upper()
    if resposta == "N":
        break
print(f"Foram cadastradas {len(pessoas)} pessoas")
print(f"O maior peso foi de {maiorPeso}Kg. Peso de ", end="")
for p in pessoas:
    if p[1] == maiorPeso:
        print(f"[{p[0]}] ", end="")
print()
print(f"O menor peso foi de {menorPeso}Kg de ", end="")
for p in pessoas:
    if p[1] == menorPeso:
        print(f"[{p[0]}] ", end="")
print()