def real(i=0):
    return f'R${i:.2f}'.replace('.', ',')


def aumentar(i, por=0, foreal=True):
    """
    :param foreal: Para mostrar ou não o valor formatado em dinheiro
    :param i: Valor a ser aumentado
    :param por: Porcentagem a ser aumentada
    :return: O valor atualizado
    """
    if foreal is True:
        return real(i + (i * (por / 100)))
    else:
        return i + (i * (por / 100))


def diminuir(i, por=0, foreal=True):
    """
    :param foreal: Para mostrar ou não o valor formatado em dinheiro
    :param i: Valor a ser diminuido
    :param por: Porcentagem a ser diminuida
    :return: O valor atualizado
    """
    if foreal is True:
        return real(i - (i * (por/100)))
    else:
        return i - (i * (por/100))


def dobro(i, foreal=True):
    if foreal is True:
        return real(i * 2)
    else:
        return i * 2


def metade(i, foreal=True):
    if foreal is True:
        return real(i / 2)
    else:
        return i / 2
