number = int(input("Write a number between 0 and 9999: "))

unit = number // 1 % 10
ten = number // 10 % 10
hundred = number // 100 % 10
thousands = number // 1000 % 10

print("""Analyzing the number {}
Unidade: {}
Dezena: {}
Centena: {}
Milhar: {}""".format(number, unit, ten, hundred, thousands))