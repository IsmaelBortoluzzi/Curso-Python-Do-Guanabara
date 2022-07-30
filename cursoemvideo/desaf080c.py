from typing import List

li = []

for i in range(5):
    j = int(input(f'{i} Número'))
    if i == 0 or j > li[-1]:
        li.append(j)
        print('O valor foi adicionado ao final da lista.')
    else:
        for c in range(5):
            if j < li[c]:
                li.insert(c, j)
                print(f'O número foi adicionado na posição {c}')
                break
print(li)
