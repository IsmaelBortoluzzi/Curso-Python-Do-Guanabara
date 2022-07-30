# Contagem por extenso

nums = ('zero', 'um', 'dois', 'três', 'quatro',
        'cinco', 'seis', 'sete', 'oito',
        'nove', 'dez')

"""lisnums = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

esco = int(input('Digite um número de 0 a 10 que '
                 'queira ver por extenso: '))

while esco not in lisnums:
    esco = int(input('Digite um número de 0 a 10 que '
                     'queira ver por extenso: '))"""
while True:
    while True:
        esco = int(input('Digite um número de 0 a 10 que '
                         'queira ver por extenso: '))
        if 0 <= esco <= 10:
            break
        print('Tente novamente.', end=' ')

    print(esco, nums[esco])

    c = str(input('Quer continuar?')).strip().upper()[0]
    if c == 'N':
        break
