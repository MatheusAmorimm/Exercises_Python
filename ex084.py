pessoas = []
dados = []
maiorPeso = 0
menorPeso = 0
contador = 0
pesados = list()
leves = list()
while True:
    dados.append(str(input("Nome: ")))
    dados.append(float(input("Peso: ")))
    if contador == 0:
       maiorPeso = menorPeso = dados[1]
    else:
        if dados[1] >= maiorPeso:
            maiorPeso = dados[1]
            pesados.append(dados[:])
        if dados[1] < menorPeso:
            menorPeso = dados[1]
            leves.append(dados[:])
    pessoas.append(dados[:])
    dados.clear()
    resposta = str(input("Deseja cadastrar uma nova pessoa? [S/N]")).strip().upper()
    while resposta != "S" and resposta != "N":
        resposta = str(input("Tente Novamente. Deseja cadastrar uma nova pessoa? [S/N]")).strip().upper()
    if resposta == "N":
        break
    contador += 1
print(f"Foram cadastradas {len(pessoas)} pessoas")
print(f"O maior peso foi de {maiorPeso}Kg", end="")
for pessoas in pesados:
    print(pessoas[0], end=" ")
print(f"O menor peso foi de {menorPeso}Kg. Peso de {leves[0][0]}")