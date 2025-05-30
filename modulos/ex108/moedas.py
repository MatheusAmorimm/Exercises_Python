def dobro(price = 0):
    double = price * 2
    return double

def metade(price = 0):
    piece = price/2
    return piece

def aumentar(price = 0, percent = 0):
    juros = price + (price * (percent/100))
    return juros

def diminuir(price = 0, percent = 0):
    desconto = price - (price * (percent/100))
    return desconto

def moeda(price = 0, unit = 'R$'):
    return f'{unit}{price:.2f}'.replace('.', ',')