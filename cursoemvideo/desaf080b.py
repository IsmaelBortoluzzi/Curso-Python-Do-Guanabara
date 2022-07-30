num = []

for c in range(5):
    n = int(input('Número: '))
    if c == 0 or n > num[-1]:
        num.append(n)
        print('O número foi adicionado no final da lista.')
    else:
        for i in range(5):
            if n <= num[i]:
                num.insert(i, n)
                print(f'O número foi adicionado na posição {i}.')
                break
print(num)
