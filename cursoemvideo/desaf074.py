# Maior e menor número na tupla

from random import randint

print('Gerador de números aleatórios ')

nums = ()

for _ in range(5):
    nums += (randint(0, 9),)

print(nums)
print(f'O Maior número gerado foi o {max(nums)}')
print(f'O menor número gerado foi o {min(nums)}')
