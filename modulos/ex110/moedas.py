def dobro(price = 0, formated=False):
    """
    :param price: valor a ser dobrado
    :param formated: se vai ser formatado como moedas ou não, usando "True" or "False"
    :return: retorna o dobro do param price
    """
    double = price * 2
    return double if formated == False else moeda(double)

def metade(price = 0, formated=False):
    """
    :param price: valor a ser dividido por 2
    :param formated: se vai ser formatado como moedas ou não, usando "True" or "False"
    :return: retorna a metade do valor
    """
    piece = price/2
    return piece if formated == False else moeda(piece)

def aumentar(price = 0, percent = 0, formated=False):
    """
    :param price: valor a ser aumentado
    :param percent: a taxa que vai ser incrementada ao valor
    :param formated: se vai ser formatado como moedas ou não, usando "True" or "False"
    :return: retorna o valor acrescido da taxa solicitada
    """
    juros = price + (price * (percent/100))
    return juros if formated == False else moeda(juros)

def diminuir(price = 0, percent = 0, formated=False):
    """
    :param price: valor que vai sofrer redução
    :param percent: taxa que vai ser descontada do valor
    :param formated: se vai ser formatado como moedas ou não, usando "True" or "False"
    :return: retorna o valor com o desconto solicitado
    """
    desconto = price - (price * (percent/100))
    return desconto if formated == False else moeda(desconto)

def moeda(price = 0, unit = 'R$'):
    """
    :param price: valor que vai ser formatado
    :param unit: moedas que vai ser utilizada
    :return: retorna o valor formatado como moedas
    """
    return f'{unit}{price:.2f}'.replace('.', ',')

def resumo(price = 0, taxaj = 10, taxad = 5):
    """
    :param price: valor a ser resumido
    :param taxaj: taxa de juros a ser acrescido
    :param taxad: taxa de desconto a ser aplicado
    """
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço analisado: \t{moeda(price)}')
    print(f'Dobro do preço: \t{dobro(price, True)}')
    print(f'Metade do preço: \t{metade(price, True)}')
    print(f'{taxaj}% de juros: \t\t{aumentar(price, taxaj, True)}')
    print(f'{taxad}% de desconto: \t{diminuir(price, taxad, True)}')
    print('-'*30)
