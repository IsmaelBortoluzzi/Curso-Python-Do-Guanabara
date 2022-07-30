# MEGA SENA (MEGA FRAUDE*)vAlfa

from random import randint
from time import sleep

print('{:-^30}'.format(' Números da \033[35mMega Sena\033[m '))

j = int(input('\nQuantos palpites tu queres? '))
print('')

for c in range(j):
    lista = []
    cont = 0

    while cont != 6:
        igual = False
        h = randint(1, 60)
        for i in range(len(lista)):
            if h == lista[i]:
                igual = True
                cont -= 1
                break
        if igual is False:
            lista.append(h)
        cont += 1

    print(f'\033[34m{lista}', '\n', '\033[30m-='*11)
    sleep(0.75)
