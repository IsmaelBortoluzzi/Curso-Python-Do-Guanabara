# Máquina caça-níquel v2.0

import random

ran = random.randint(1, 5)
palp = int(input('Escolha um número de 1 até 5:').isnumeric())
contador = 1

while True:
    if palp > 5:
        print('Palpite inválido. Tente novamente.')
        palp = int(input('Escolha um número de 1 até 5:'))
    else:
        if palp == ran and contador == 0:
            print('Certa resposta! háhá')
            break
        elif palp == ran and contador != 0:
            print('Certa resposta hahá')
            print('Você precisou de {} tentativas para acertar.'
                  .format(contador))
            break
        else:
            print('ERRRROOOUUU')
            contador = contador + 1
            palp = int(input('Escolha um número de 1 até 5:'))
