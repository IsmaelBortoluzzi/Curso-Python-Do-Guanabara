# Utilizando Pacotes agora

def titulo(t):
    print('-'*len(t))
    print(f'{t}')
    print('-'*len(t))


def resumo(valor, por_a=0, por_d=0):
    """
    :param valor: valor a ser analisado
    :param por_a: porcentagem de aumento
    :param por_d: porcentagem de diminuiução
    :return: múltiplas funções
    """
    dicionario = dict()
    titulo('         Resumo Do Valor         ')
    dicionario['Preço Analisado:'] = real(valor)
    dicionario[f'{por_a}% de aumento:'] = aumentar(valor, por_a)
    dicionario[f'{por_d}% de redução:'] = diminuir(valor, por_d)
    dicionario[f'O dobro de {valor}:'] = (dobro(valor))
    dicionario[f'A metade de {valor}:'] = (metade(valor))
    for k, v in dicionario.items():
        print(f'{k:<20} {v}')
    print('-'*len('         Resumo Do Valor         '))


def real(i=0):
    try:
        return f'R${i:.2f}'.replace('.', ',')
    except:
        return 'O valor não pode ser convertido para formato moeda.'


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

