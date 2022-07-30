# Lista ordenada sem o sort

num = []
i = 0

for i in range(5):
    n = int(input(f'Digite o {i} número: '))
    if i == 0 or n > num[-1]:
        num.append(n)
        print('O número foi adicionado ao final da lista')
    else:
        pos = 0
        while pos < len(num):
            if n <= num[pos]:
                num.insert(pos, n)
                print(f'O número foi adicionado na posição {pos}.')
                break
            pos += 1
print(num)
