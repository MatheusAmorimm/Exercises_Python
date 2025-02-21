valores = list()

for contador in range(0, 5):
    valores.append(int(input(f"Digite um valor para casa {contador}:  ")))

maior = max(valores)
menor = min(valores)

print(f"O maior valor digitado foi: {maior}, na casa {valores.index(maior)}\nE o menor valor foi {menor} na casa {valores.index(menor)}")

