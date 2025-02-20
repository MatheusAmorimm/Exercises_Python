soma = 0
contador = 0
while True:
    number = int(input("Digite um valor \033[1;33m(use 999 para encerrar)\033[m: "))
    if number != 999:
        soma += number
        contador += 1
    else:
        break

print(f'Voce digitou {contador} valores e a soma entre eles e: {soma} ')