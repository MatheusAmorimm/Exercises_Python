valoresTotais = list()
valoresPares = list()
valoresImpares = list()

while True:
    valor = int(input("Digite um valor: "))
    valoresTotais.append(valor)
    resposta = str(input("Deseja continuar? [S/N] ")).strip().upper()[0]
    if valor % 2 == 0:
        valoresPares.append(valor)
    else:
        valoresImpares.append(valor)
    while resposta != "S" and resposta != "N":
        resposta = str(input("Tente novamente. Deseja continuar? [S/N] ")).strip().upper()[0]
    if resposta == "N":
        break

print(f"""Valores adicionados: {valoresTotais}
Valores pares: {valoresPares}
Valores Impares: {valoresImpares}""")