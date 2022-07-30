from random import randint
from time import sleep
from operator import itemgetter

print('{:-^20}'.format('JOGO DE DADOS'))

nums = dict()
ranking = list()

x = input('Pressione "enter" para começar')
print('')

for i in range(4):
    nums[f'jogador_{i+1}'] = randint(1, 6)

print('Valores sorteados')
for k, v in nums.items():
    print(f'O {k} tirou {v} nos dados.')
    sleep(1.00)

ranking = sorted(nums.items(), key=itemgetter(1), reverse=True)

print('-='*25)

for i, v in enumerate(ranking):
    print(f'O {v[0]} ficou em {i+1}° lugar com {v[1]} pontos',  end='')
    print('')
    sleep(1)
