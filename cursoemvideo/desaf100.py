# Sorteano números e sorteando os pares

from random import randint
from time import  sleep


def sorteia(lista):
    for i in range(5):
        lista.append(randint(1, 1000))
        print(lista[-1], end=' ')
        sleep(0.3)
    print('\n')


def somapar(lista):
    soma = 0
    for i in lista:
        if i % 2 == 0:
            soma += i
    print(soma)


numeros = []

print('Sorteando 5 números: ', end='')
sorteia(numeros)
print('A soma dos pares é ', end='')
somapar(numeros)
