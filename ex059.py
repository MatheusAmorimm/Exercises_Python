from time import sleep

number1 = float(input("Digite um numero: "))
number2 = float(input("Digite outro numero: "))
menu = 0
maior = 0
if number1 > number2:
    maior = number1
elif number1 < number2:
    maior = number2
print("=" * 20)
while menu != 5:
    menu = int(input("""Escolha uma opcao:
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos Numeros
[5] Sair
>>>>> OPCAO: """))
    print("=" * 20)
    if menu == 1:
        print("A soma entre {} e {} resulta em: {}".format(number1, number2, number1 + number2))
        print("=" * 20)
    elif menu == 2:
        print("O produto entre {} e {} é: {}".format(number1, number2, number1 * number2))
        print("=" * 20)
    elif menu == 3:
        if number1 == number2:
            print("Os numeros sao iguais")
            print("=" * 20)
        else:
            print("O maior numero entre {} e {} é: {}".format(number1, number2, maior))
            print("=" * 20)
    elif menu == 4:
        number1 = float(input("Digite um numero: "))
        number2 = float(input("Digite outro numero: "))
        if number1 > number2:
            maior = number1
        elif number1 < number2:
            maior = number2
    elif menu == 5:
        print("Finalizando...")
        print("=" * 20)
    else:
        print("Opcao invalida. Tente novamente")
        print("=" * 20)
sleep(1)
print('FIM')