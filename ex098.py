from time import sleep


def divisor():
    print("-"*30)

def counter(init, end, pas):

    if pas < 0:
        pas = abs(pas)

    if pas == 0:
        pas = 1

    if init < end:
        cont = init
        while cont <= end:
            print(cont, end=" ")
            sleep(0.2)
            cont += pas
        print()
    else:
        cont = init
        while cont >= end:
            print(cont, end=" ")
            sleep(0.2)
            cont -= pas
        print()



counter(1,10,1)
counter(10, 0, 1)

initial = int(input("Em qual numero comeca a contagem: "))
lastnum = int(input("Em qual numero se encerra: "))
step = int(input("De quantos em quantos numeros: "))

counter(initial, lastnum, step)