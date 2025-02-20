number = int(input("Digite um numero para calcular seu fatorial: "))
fac = 1
contador = number
print("Calculando {}!".format(number), end=" ")
while contador > 0:
    print("{}".format(contador), end='')
    print(" x " if contador > 1 else " = ", end="")
    fac *= contador
    contador -= 1
print("{}".format(fac))

