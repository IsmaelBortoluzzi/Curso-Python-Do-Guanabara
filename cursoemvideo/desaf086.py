# Fazendo uma matriz

mat = [[], [], []]

for c in range(3):
    j = int(input(f'Dige o valor para a posição [{0, c}]: '))
    mat[0].append(j)
for c in range(3):
    j = int(input(f'Dige o valor para a posição [{1, c}]: '))
    mat[1].append(j)
for c in range(3):
    j = int(input(f'Dige o valor para a posição [{2, c}]: '))
    mat[2].append(j)

print('-='*25)

for i in mat[0]:
    print(f'[ {i:^5} ]', end=' ')
print('')

for i in mat[1]:
    print(f'[ {i:^5} ]', end=' ')
print('')

for i in mat[2]:
    print(f'[ {i:^5} ]', end=' ')
