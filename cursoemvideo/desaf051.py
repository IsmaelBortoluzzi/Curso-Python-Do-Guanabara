# Progressão aritmética

print('Calculador de PA')

p = int(input('Digite o primeiro número da PA:'))
r = int(input('Digite a razão da PA:'))
en = p + (11-1) * r

for c in range(p, en, r):
    print('{}'.format(c), end=' ')
