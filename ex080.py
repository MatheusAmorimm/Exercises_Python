valores = list()

for cont in range(0,5):
    valor = int(input("Digite um valor: "))
    if cont == 0:
        print("caiu aq")
        valores.append(valor)
        print(valores)
    if valor < valores[0]:
        print("caiu aq1")
        valores.insert(0, valor)
        print(valores)
    if valor > valores[0]:
        if valores[0] < valor < valores[1]:
            print("caiu aq3")
            valores.insert(1, valor)
            print(valores)
        if valores[0] < valor > valores[1] and valor < valores[2]:
            print("caiu aq4")
            valores.insert(2, valor)
            print(valores)
        if valores[1] < valor > valores[2]:
            print("caiu aq5")
            valores.insert(3, valor)
        if valores[1] < valor < valores[2]:
            print("caiu aq5")
            valores.insert(2, valor)
        if valores[2] < valor < valores[3]:
            print("caiu aq6")
            valores.insert(3, valor)
        if valor > valores[-1]:
            print("caiu aq7")
            valores.append(valor)
            print(valores)

print(valores)