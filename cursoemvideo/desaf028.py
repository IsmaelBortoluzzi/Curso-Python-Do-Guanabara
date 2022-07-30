# Criando uma máquina caça-níquel

import random

var = random.randint(1, 5)
e = int(input('Escolha um número de 0 até 5:'))

if e == var:
    print('Certa resposta! háhá')
else:
    print('ERRRROOOUUU')
