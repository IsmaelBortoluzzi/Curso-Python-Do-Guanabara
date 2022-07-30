# Função que aceita apenas float sem retornar erro.

def readmoney(value):
    valido = False
    while not valido:
        entrada = str(input(value)).replace(',', '.').strip()
        if entrada.isalpha() or entrada.strip() == '':
            print(f'ERRO. "{entrada}" é um preço inválido.')
        else:
            valido = True
            return float(entrada)


def leiaint(i=''):
    while True:
        try:
            entrada = int(input(i))
        except KeyboardInterrupt:
            print('O usuário preferiu não informar o valor')
            return 0
        except:
            print('Você não digitou um número inteiro!')
            continue
        else:
            return entrada


def leiafloat(i=''):
    while True:
        try:
            entrada = float(input(i))
        except KeyboardInterrupt:
            print('O usuário preferiu não informar o valor')
            return 0
        except:
            print('O valor informado não foi um numero REAL')
            continue
        else:
            return entrada


def titulo_person(t, tam=0):
    print('-'*tam)
    print(f'{t}')
    print('-'*tam)


def titulo(t):
    print('-'*len(t))
    print(f'{t}')
    print('-'*len(t))