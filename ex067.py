from time import sleep

while True:
    contador = 1
    number = int(input("Qual tabuada deseja saber: "))
    if number < 0:
        print('*' * 20)
        print('Finalizando...')
        sleep(1)
        print('Acabou')
        break
    print('*' * 20)
    while contador < 11:
        print(f'{number} x {contador:2} = {number * contador}')
        contador += 1
    print('*' * 20)