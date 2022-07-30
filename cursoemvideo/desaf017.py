# Calcula a hipotenusa com base nos valores de ca e co

from math import sqrt

co = float(input('Insira o comprimento do cateto oposto em cm:'))
ca = float(input('Insira o comprimento do cateto adjacente em cm:'))
h = sqrt((co ** 2) + (co ** 2))
print('A hipotenusa do triângulo retângulo '
      'é igual a {:.3f}cm'.format(h))
