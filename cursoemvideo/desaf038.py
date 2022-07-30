# escolhendo o maior número

n1 = int(input('Escolha um número:'))
n2 = int(input('Escolha outro número:'))

if n1 > n2:
    print('O número {} é maior do que {}.'.format(n1, n2))
elif n1 < n2:
    print('O número {} é maior do que {}.'.format(n2, n1))
else:
    print('Ambos os números possuem o mesmo valor!')