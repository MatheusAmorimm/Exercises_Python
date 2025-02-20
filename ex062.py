firstTerm = int(input('insert a first term of the PA: '))
ratio = int(input('What is the ration for arithmetic progession? '))
contador = 1
total = 0
termos = 10

while termos != 0:
    total += termos
    while contador != total:
        firstTerm += ratio
        contador += 1
        print('{}'.format(firstTerm), end='')
        print(" -> " if contador != total else ". ", end="")
    termos = int(input("\nVoce deseja ver mais quantos termos? "))
    if termos == 0:
        print('-=-' * 20)
        print("A progressao terminou em: {} termos".format(contador))
