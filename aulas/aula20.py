""" Funções Parte 1 """

# Jeito chato:
a = 4
b = 5
s = a + b
print(s)
print('')
a = 4
b = 5
s = a + b
print(s)
print('')
a = 4
b = 5
s = a + b
print(s)

#  Jeito Simplificado
print('-='*25)

"""
def soma(a, b):
    s = a + b
    print(s)
    print('')


soma(3, 4)
soma(b=7, a=9)
soma(a=3, b=5)
"""

"""
def soma(a, b):
    print(f'A = {a} e B = {b}')
    print(f'A soma de A + B é igual a {a+b}')


soma(2, 7)
"""

"""
# Desempacotamento para receber vários valores:


def soma(*num):
    print(sum(num))


soma(2, 3, 77)
soma(434, 543, 777)
"""

# UTILIZANDO FUNÇÃO EM LISTA


def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1


valores = [2, 7, 4, 9, 8, 5]
print(valores)
dobra(valores)
print(f'\n{valores}')
