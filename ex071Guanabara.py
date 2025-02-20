valorRestante = 0
saldo = int(input("Digite o valor do saque: "))
total = saldo
notas = 50
totalNotas = 0

while True:
    if total >= notas:
        total -= notas
        totalNotas += 1
    else:
        if totalNotas > 0:
            print(f"Total de {totalNotas} notas de R$ {notas}")
        if notas == 50:
            notas = 20
        elif notas == 20:
            notas = 10
        elif notas == 10:
            notas = 1
        totalNotas = 0
        if total == 0:
            break
