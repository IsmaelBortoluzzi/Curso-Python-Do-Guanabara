# MEGA SENA (MEGA FRAUDE*)v2.0

from random import randint
from time import sleep

print('{:-^30}'.format(' Números da \033[31mMega Sena\033[m '))

j = int(input('\nQuantos palpites tu queres? '))
print('')

for c in range(j):
    lista = []
    i = 0

    while i < 6:
        h = randint(1, 60)
        if h not in lista:
            lista.append(h)
            i += 1
        # elif lista.count(h) != 0:
            # i -= 1
    print(f'\033[35mJogo {c+1}:\033[m ', end='')
    print(f'\033[36m{lista}', '\n', '\033[35m-='*16)
    sleep(0.75)
