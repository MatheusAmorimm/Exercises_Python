number = soma = media = contador = 0
resposta = ""
maior = 0
menor = 0
while resposta != "N":
    number = int(input("Digite um numero: "))
    resposta = str(input("Deseja continuar? [S/N] ")).strip().upper()[0]

    contador += 1
    soma += number
    media = soma / contador
    if contador == 1:
        maior = number
        menor = maior
    if number < menor:
        menor = number
    if number > maior:
        maior = number

print("Voce digitou {} valores e a media foi {}".format(contador, media))
print("O maior valor foi: {} e o menor foi: {}".format(maior, menor))