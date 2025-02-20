from random import randint
from time import sleep

vitoria = 0
derrota = 0
numeroDoPC = 0
numeroPlayer = 0
decisao = "P"
resultado = 0

while decisao == "P" or decisao == "I":
    decisao = str(input("Par ou impar? [P/I] ")).strip().upper()[0]
    numeroDoPC = randint(0,10)
    print("Escolhendo um numero...")
    sleep(1)
    print("Escolhi")
    print(numeroDoPC)
    print('*' * 20)
    numeroPlayer = int(input("Qual numero voce joga? "))
    if decisao == 'P':
        resultado = numeroDoPC + numeroPlayer
        if resultado % 2 == 0:
            vitoria += 1
            print("Voce venceu!")
            print('*' * 20)
        else:
            print("Eu venci essa!")
            derrota += 1
            print('*' * 20)
            break
    elif decisao == "I":
        resultado = numeroDoPC + numeroPlayer
        if resultado % 2 != 0:
            vitoria += 1
            print("Voce venceu")
            print('*' * 20)
        else:
            print("Eu venci essa!")
            derrota += 1
            print('*' * 20)
            break

print("Finalizando...")
print("Contabilizando vitorias e derrotas...")
sleep(1)
print('*' * 20)

print(f'Voce teve: {vitoria} vitorias e {derrota} derrotas')