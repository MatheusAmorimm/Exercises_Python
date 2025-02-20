from random import randint
"""maior = 0
menor = 0"""

numeros = randint(0,10), randint(0, 10), randint(0,10), randint(0, 10), randint(0, 10)

"""for numero in range(len(numeros)):
    if numero == 0:
        maior = numeros[numero]
        menor = maior
    if maior < numeros[numero]:
        maior = numeros[numero]
    if menor > numeros[numero]:
        menor = numeros[numero]
"""
for numero in range(len(numeros)):
    print(numeros[numero], end=" ")

print(f"""\nO maior foi: {max(numeros)}
E o menor valor foi: {min(numeros)}""", end="")
