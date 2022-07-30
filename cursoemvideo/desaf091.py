from random import randint
from time import sleep

print('{:-^20}'.format('JOGO DE DADOS'))

nums = dict()
resul = []

x = input('Pressione "enter" para começar')
print('')

for i in range(4):
    resul.append(randint(1, 6))

for i, c in enumerate(resul):
    nums[f'jogador_{i+1}'] = resul[i]

for j, n in nums.items():
    print(f'O {j} tirou {n}')
    sleep(1.75)
nums.clear()

print('-='*25)

resul.sort(reverse=True)

cont = 1
for j, n in nums.items():
    print(f'{cont}° lugaer: {j} com {n}')
    cont = cont+1
    sleep(1.75)

