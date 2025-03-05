matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_par = maior = soma_coluna = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f"Digite um valor para [{linha}, {coluna}]: "))
for linha in range(0, 3):
    for coluna in range(0,3):
        print(f"[{matriz[linha][coluna]:^5}]", end="")
        if matriz[linha][coluna] % 2 == 0:
            soma_par += matriz[linha][coluna]
    print()
print(f"A soma de todos os pares e: {soma_par}")
for linha in range(0,3):
    soma_coluna += matriz[linha][2]
print(f"A soma dos valores da terceira coluna e: {soma_coluna}")
for coluna in range(0,3):
    if coluna == 0 or matriz[1][coluna] > maior:
         maior = matriz[1][coluna]
print(f"O maior numero da coluna 2 e: {maior}")
