from time import sleep

valores = list()
resposta = ""
while True:
    valor = int(input("Digite um valor: "))
    if valor in valores:
        print("Valor duplicado, nao foi possivel adicionar.")
        print("------ // ------")
        break
    else:
        valores.append(valor)
        print("Valor adicionado com sucesso!")
        print("------ // ------")
    resposta = str(input("Voce deseja continuar? [S/N] ")).strip().upper()[0]
    while resposta != "S" and resposta != "N":
        print("Resposta invalida, tente novamente")
        resposta = str(input("Voce deseja continuar? [S/N] ")).strip().upper()[0]
    if resposta == "N":
        break
print("------ // ------")
print("Finalizando...")
sleep(1)
print(f"Voce digitou o(s) valor(es): {sorted(valores)}")
