# Sorteando um aluno na lista

import random

n1 = int(input('Digite o número designado'
               ' ao primeiro aluno da contagem:'))
n2 = int(input('Digite o número designado'
               'ao último aluno da contagem:'))

r = random.randint(n1, n2)
print('O aluno escolhido é o de número: {}'.format(r))
