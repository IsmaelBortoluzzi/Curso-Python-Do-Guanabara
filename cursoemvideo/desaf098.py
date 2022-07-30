# Função de contador

from time import sleep


def contador(i, f, p):
    for c in range(i, f, p):
        print(c, end=' ')
        sleep(0.50)
    print('\n')


contador(10, 20+1, 1)
contador(20, 10-1, -2)

print('--------')
print('Sua vez')
print('--------\n')

ini = int(input('Digite o início: '))
fin = int(input('Digite o final:  '))
pas = int(input('digite o passo:  '))
print('')

if ini < fin:
    if pas <= 0:
        pas = 1
    print(f'Contagem de {ini} até {fin} de {pas} em {pas}\n')
    contador(ini, fin + 1, pas)

if ini > fin:
    if pas == 0:
        pas = -1
    if pas > 0:
        pas *= -1
    print(f'Contagem de {ini} até {fin} de {pas*-1} em {pas*-1}\n')
    contador(ini, fin-1, pas)
