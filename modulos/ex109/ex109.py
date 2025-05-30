import moedas
number = float(input("Digite o valor: R$ "))

print(f"A metade de {moedas.moeda(number)} e {moedas.metade(number, True)}")
print(f"O dobro de {moedas.moeda(number)} e {moedas.dobro(number, True)}")
print(f"Aumentando 10%, temos {moedas.aumentar(number,10, True)}")
print(f"Reduzindo 13%, temos {moedas.diminuir(number, 13, True)}")