def moeda(price = 0, unit = 'R$'):
    """
    :param price: valor que vai ser formatado
    :param unit: moedas que vai ser utilizada
    :return: retorna o valor formatado como moedas
    """
    return f'{unit}{price:.2f}'.replace('.', ',')