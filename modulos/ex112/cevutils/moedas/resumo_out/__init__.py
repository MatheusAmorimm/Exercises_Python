from modulos.ex112.cevutils import moedas as mds

def resumo(price = 0, taxaj = 10, taxad = 5):
    """
    :param price: valor a ser resumido
    :param taxaj: taxa de juros a ser acrescido
    :param taxad: taxa de desconto a ser aplicado
    """
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço analisado: \t{mds.format.moeda(price)}')
    print(f'Dobro do preço: \t{mds.dobro(price, True)}')
    print(f'Metade do preço: \t{mds.metade(price, True)}')
    print(f'{taxaj}% de juros: \t\t{mds.aumentar(price, taxaj, True)}')
    print(f'{taxad}% de desconto: \t{mds.diminuir(price, taxad, True)}')
    print('-'*30)