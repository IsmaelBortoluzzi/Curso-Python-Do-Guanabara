# Sistema PyHelp com cores

c = ['\033[m',
     '\033[36m',
     '\033[31m',
     '\033[34m',
     '\033[32m',
     '\033[33m']


def titulo(t, cor=0):
    print(c[cor])
    print('-'*len(t))
    print(t)
    print('-'*len(t))
    print(c[0])


def pyhelp(j, corhelp=0):
    print(c[corhelp])
    return f'{help(j)}'


while True:
    titulo('Sistema de ajuda Pyhelp', cor=1)

    q = str(input('Função ou Biblioteca: '))

    if q.strip().upper() in 'FIM':
        titulo('Até Logo', cor=2)
        break

    titulo(f'Acessando o Manual do Comando {q}', 3)
    pyhelp(q, corhelp=5)
