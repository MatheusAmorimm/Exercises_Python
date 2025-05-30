import moedas
number = float(input("Digite o valor: R$ "))

print(f"A metade de R$ {number} e R${moedas.metade(number)}")
print(f"O dobro de R${number} e R${moedas.dobro(number)}")
print(f"Aumentando 10%, temos {moedas.aumentar(number, 10)}")