maiorPeso = 0
menorPeso = 0
for p in range(1,6):
    peso = float(input("Qual o peso da {}º pessoa? ".format(p)))
    if p == 1:
        maiorPeso = peso
        menorPeso = peso
    else:
        if peso > maiorPeso:
            maiorPeso = peso
        if peso < menorPeso:
            menorPeso = peso

print('menor peso: {}    maior peso: {}'.format(menorPeso, maiorPeso))