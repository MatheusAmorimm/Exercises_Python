valores = []
while True:
    valor = int(input("Digite um valor: "))
    print("Valor inserido com sucesso...")
    valores.append(valor)
    response = str(input("Voce deseja continuar? [S/N] ")).strip().upper()[0]
    while response != "S" and response != "N":
        response = str(input("Tente novamente. Voce deseja continuar? [S/N]")).strip().upper()[0]
    if response == "N":
        break
valores.sort(reverse=True)
print(f"""Voce digitou {len(valores)} numeros
Os numeros adicionados de forma decrescente ficam assim: {valores}\n""", end="")
if 5 in valores:
    print("O valor 5 foi digitado")
else:
    print("O valor 5 nao foi digitado")