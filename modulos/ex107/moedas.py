def dobro(price):
    double = price * 2
    return double

def metade(price):
    piece = price/2
    return piece

def aumentar(price, percent):
    juros = price + (price * (percent/100))
    return juros

def diminuir(price, percent):
    desconto = price - (price * (percent/100))
    return desconto
