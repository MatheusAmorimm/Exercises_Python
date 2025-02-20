from math import trunc

number = float(input("Write a rational number: "))
formated_number = trunc(number)

print("The number {} have a integer part {}". format(number, formated_number))