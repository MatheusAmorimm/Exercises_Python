import moedas
number = float(input("Digite o valor: R$ "))

print(f"A metade de {moedas.moeda(number)} e {moedas.moeda(moedas.metade(number))}")
print(f"O dobro de {moedas.moeda(number)} e {moedas.moeda(moedas.dobro(number))}")
print(f"Aumentando 10%, temos {moedas.moeda(moedas.aumentar(number,10))}")