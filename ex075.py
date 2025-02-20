pares = 0

numeros = (int(input("Digite um numero: ")), int(input("Digite outro numero: ")), int(input("Digite mais numero: ")), int(input("Digite o ultimo numero: ")))

print(f"O numero 9 apareceu {numeros.count(9)} vezes")
if 3 in numeros:
    print(f"O primeiro numero 3 apareceu na posicao {numeros.index(3) + 1}")
else:
    print("O valor 3 nao foi digitado")
print("Os numeros pares foram: ", end="")

for numero in range(len(numeros)):
    if numeros[numero] % 2 == 0:
        print(numeros[numero], end=" ")
