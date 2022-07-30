# Estrutura de repetição FOR

for c in range(0, 3):
    print('vagabundo')
print('fim')

for c in range(7, 0, -1):
    print(c)
print('fim')

for c in range(16, -1, -2):
    print(c)
print('fim')

for c in range(0, 14, 2):
    print(c)
print('fim')

n = int(input('Digite um número:'))
for c in range(0, n+1):
    print(c)
print('fim')

i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))

for c in range(i, f+1, p):
    print(c)
print('Fim')

s = 0
for c in range(0, 3):
    n = int(input('Digite um número:'))
    s = s + n
print(s)
print('fim')
