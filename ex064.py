contador = soma = 0
flag = int(input("Digite um numero: "))
while flag != 999:
    soma += flag
    contador += 1
    flag = int(input("Digite um numero: "))
print('Voce digitou {} numeros e a soma entre eles foi: {}'.format(contador, soma))