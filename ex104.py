def readInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print("Erro! Digite um numero inteiro valido.")
        if ok:
            break
    return valor

number = readInt('Digite um numero inteiro: ')
print(f"Voce digitou o numero: {number}")