valorRestante = 0
notas1 = 0
saldo = int(input("Digite o valor do saque: "))

while True:
    if saldo // 50 < 1:
        notas50 = 0
        valorRestante = saldo
    else:
        notas50 = saldo // 50
        valorRestante = saldo - (notas50 * 50)
    if valorRestante != 0  and valorRestante // 20 < 1:
        notas20 = 0
    else:
        notas20 = valorRestante // 20
        valorRestante = valorRestante - (notas20 * 20)
    if valorRestante != 0 and valorRestante// 10 < 1:
        notas10 = 0
    else:
        notas10 = valorRestante // 10
        valorRestante = valorRestante - (notas10 * 10)

    if valorRestante != 0:
        while valorRestante != 0:
            valorRestante -= 1
            notas1 += 1
        break
    else:
        break

print(f"Voce sacou {notas50} notas de 50, {notas20} notas de 20, {notas10} notas de 10 e {notas1} moedas de 1 real")

