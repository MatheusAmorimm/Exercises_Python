from time import sleep

numeros = "zero","um","dois", "tres", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte"

numero = int(input("Digite um numero entre 0 e 20: "))
resposta = ""

while True:
    while numero < 0 or numero > 20:
        numero = int(input("Tente novamente. Digite um numero entre 0 e 20: "))
    print(f"Voce digitou o numero: {numeros[numero]}")
    print("----- // -----")
    resposta = str(input("Voce deseja continuar ? [S/N] ")).strip().upper()[0]
    print("----- // -----")
    while resposta != "S" and resposta != "N":
        resposta = str(input("Tente novamente. Voce deseja continuar ? [S/N]" )).strip().upper()[0]
    if resposta == "S":
        numero = int(input("Digite um numero entre 0 e 20: "))
    if resposta == "N":
        break
print("----- // -----")
sleep(1)
print("FIM DO PROGRAMA")