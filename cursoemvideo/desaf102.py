# MERDA de fatorial de novo

def fatorial(num, show=False):
    """
    fatorialin, show=False
    :param num: Número a ser calculado
    :param show: (Opcional) mostrar ou não a conta
    :return: O valor do fatorial de um número n
    """
    f = 1
    for i in range(num, 0, -1):
        f = f * i
        if show is True:
            print(i, end='')
            if i > 1:
                print(f' x ', end='')
            else:
                print(f' = ', end='')
    return f


while True:
    j = int(input('num'))
    print(fatorial(j, show=True))
    help(fatorial)
