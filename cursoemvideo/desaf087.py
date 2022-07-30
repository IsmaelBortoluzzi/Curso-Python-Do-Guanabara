# Mostrando matrizes v3.0

nums = [[], [], []]
som_par = 0
som_3c = 0
mai2 = 0

for i in range(3):
    for c in range(3):
        j = int(input(f'Digite o valor da posição [{i, c}]: '))
        nums[i].append(j)

print('-='*25)

for i in range(3):
    for c in range(3):
        print(f'[{nums[i][c]:^5}]', end=' ')
    print('')

print('-='*25)

for i in nums:
    for c in i:
        if c % 2 == 0:
            som_par = som_par + c
    som_3c = som_3c + i[2]

nums[1][0] = mai2
for i in range(3):
    if nums[1][i] > mai2:
        mai2 = nums[1][i]

print(f'A soma dos pares é {som_par}')
print(f'\nA soma dos números da 3° coluna é: {som_3c}')
print(f'\nO maior número da 2 linha é o {mai2}')

print('\n\033[36m{:-^30}'.format('FIM'))
