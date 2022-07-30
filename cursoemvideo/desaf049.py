# Tabuada v 2.0

print('TABUADA V2.0')

n = int(input('Digite de que número queres a tabuada: '))
m = int(input('Quer que a tabuada acabe em que número? '))

for c in range(0, m+1, 1):
    r = n * c
    print('{} x {} = {}'.format(n, c, r))
