# Módulos e pacotes:
"""
def fatorial(n):
    f = 1
    for c in (1, n+1):
        f += c
    return f


num = int(input('Digite: '))
fat = fatorial(num)
print(f'O fatorial de {num} é {fat}')


def cor(**kwargs):  # Faz o cara declarar a variável opcional e joga tudo num dicionário
    print(kwargs)
"""

"""
Ordem de declaração de parâmetros:

parâmetros OBRIGATÓRIOS
*args
parâmetros defaut
**kwargs
"""

#  Desempacotamento utilizando parametros normais:


def soma(a, b, c):
    return a + b + c


lista = [10, 20, 20]
tupla = (10, 20, 20)
dicionario = dict(a=10, b=20, c=20)
# AS CHAVES DO DICIONARIO DEVEM SER IGUAIS AOS PARÂMETROS DAS FUNÇÕES!

print(soma(*lista))
print(soma(*tupla))
print(soma(**dicionario))

# Olha o que acontece colocando as chaves erradas
dicionario2 = dict(d=10, e=20, f=20)
print(soma(dicionario2))

"-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-="

# Desempacotamento utilizando kwargs:


def nomes(**kwargs):
    return f"{kwargs['nome']}, {kwargs['sobrenome']}"


pessoas = {'nome': 'Franz', 'sobrenome': 'Jodel'}

print(nomes(**pessoas))