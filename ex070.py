from time import sleep

nomeDoBarato = ""
total = 0
produtoMais1000 = 0
menor = 0

print("=" * 40)
print("{:^40}".format("TechAmorim"))
print("=" * 40)

while True:
    nomeProduto = str(input("Nome do Produto: "))
    valor = float(input("Preço: R$ "))
    print("-" * 30)
    continuar = str(input("Deseja adicionar mais algum item? [S/N] ")).strip().upper()[0]
         # validacao de dados
    while continuar != "S" and continuar != "N":
        continuar = str(input("Deseja adicionar mais algum item? [S/N] ")).strip().upper()[0]
    print("-" * 30)
    total += valor                          #somando o valor de todas as compras

    if valor > 1000:
        produtoMais1000 += 1              #contabilizando os produtos com valor acima de 1000

    if menor == 0:
        menor = valor                            #Achando o menor valor
        nomeDoBarato = nomeProduto

    elif menor > valor:
        menor = valor
        nomeDoBarato = nomeProduto


    if continuar == "N":
        break                               #Finalizando o programa

print("Finalizando....")
sleep(1)
print("{:=^40}".format(" Carrinho "))
print(f"""O total da compra foi: R$ {total:.2f}
Ha {produtoMais1000} produtos custando mais que R$ 1.000,00
O produto mais barato do carrinho e {nomeDoBarato} que custa R${menor:.2f}""")
