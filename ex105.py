
def boletim(lst, sit=False):
    """
    --> Recebe as notas da turma, faz a media e retorna o boletim
    :param lst: Recebe uma lista de valores
    :param sit: (opcional) mostra a situacao geral, se a media for abaixo de 5 = ruim,entre 5.1 e 6.9 = aceitavel e 7 ou + = boa
    :return: retorna as notas da turma e a media.
    """
    bol = dict()
    maior = menor = soma = cont = 0

    for num in lst:
        if cont == 0:
            menor = num
        if maior < num:
            maior = num
        if menor > num:
            menor = num
        soma += num
        cont += 1
    media = soma / len(lst)
    bol["total"] = cont
    bol["maior"] = maior
    bol["menor"] = menor
    bol["media"] = media

    if sit:
        if media <= 5:
            bol["situacao"] = "Ruim"
        elif 5 < media < 7:
            bol["situacao"] = "Aceitavel"
        else:
            bol["situacao"] = "Boa"
        return bol
    else:
        return bol

resp = boletim([5.5, 9.5, 10, 6.5], sit=True)
print(resp)