valores = list()

for contador in range(0, 5):
    valores.append(int(input(f"Digite um valor para casa {contador}:  ")))

maior = max(valores)
menor = min(valores)

print(f"O maior valor digitado foi: {maior} nas posicoes: ", end="")
for indice, valor in enumerate(valores):
    if valor == maior:
        print(f"{indice}", end=" ")
print()
print(f"O menor valor digitado foi: {menor} nas posicoes", end=" ")
for indice, valor in enumerate(valores):
    if valor == menor:
        print(f"{indice}", end=" ")


