# Fazendo uma matriz v2.0

mat = [[], [], []]

for i in range(3):
    for c in range(3):
        j = int(input(f'Digite o número {i, c}: '))
        mat[i].append(j)

for i in range(3):
    for c in range(3):
        print(f'[ {mat[i][c]} ]', end=' ')
    print('')
