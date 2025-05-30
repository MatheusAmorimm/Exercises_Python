from format import moeda
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




