#Mostra numero float truncado

from math import trunc

n1 = float(input('Digite um número real (ex: 7.287):'))
print('A parte inteira de {} é {}'.format(n1, trunc(n1)))