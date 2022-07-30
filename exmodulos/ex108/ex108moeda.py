def aumentar(i, por=0):
    """
    :param i: Valor a ser aumentado
    :param por: Porcentagem a ser aumentada
    :return: O valor atualizado
    """
    return i + (i * (por/100))


def diminuir(i, por=0):
    """
    :param i: Valor a ser diminuido
    :param por: Porcentagem a ser diminuida
    :return: O valor atualizado
    """
    return i - (i * (por/100))


def dobro(i):
    return i * 2


def metade(i):
    return i / 2


def real(i):
    return f'R${i:.2f}'.replace('.', ',')
