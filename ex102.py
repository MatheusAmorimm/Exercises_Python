def fact(num, show=False):
    """
    --> Calcula o fatorial de um numero.
    :param num: recebe o numero a ser calculado
    :param show: (opcional) Mostra ou nao a conta
    :return: O valor do fatorial do param num
    """
    if show:
        contador = num
        fac = 1
        while contador > 0:
            print("{}".format(contador), end='')
            print(" x " if contador > 1 else " = ", end="")
            fac *= contador
            contador -= 1
        return fac
    else:
        fac = 1
        for cont in range(num, 0, -1):
            fac *= cont
        return fac

number = int(input("Digite o numero que deseja saber o fatorial: "))
conta = str(input("Deseja ver o calculo? [S/N]: ")).upper().strip()

if conta == "S":
    print(fact(number, True))
else:
    print(fact(number))