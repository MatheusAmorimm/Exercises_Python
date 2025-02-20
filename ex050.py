soma = 0
cont = 0
for c in range (1, 7):
    number = int(input('Enter a integer number: '))
    if number % 2 == 0:
        soma += number
        cont += 1

print('You entered {} even numbers and their sum is {}'.format(cont, soma))

