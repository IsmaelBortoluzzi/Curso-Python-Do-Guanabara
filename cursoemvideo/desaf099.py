# Função Maior
from time import sleep


def maior(*mai):
    bigger = 0
    for m in mai:
        if m > bigger:
            bigger = m
    print('Os valores passados foram:')
    for i in mai:
        print(i, end=' ')
        sleep(0.3)
    print('')
    print(f'\nForam {len(mai)} valore ao todo.\n')
    print(f'O maior valor foi o {bigger}')
    print('-='*20)


maior(43, 65, 32, 76, 96, 67, 88)
maior(32, 54, 456, 764, 67, 674, 467, 46, 75)
maior(23, 54, 65, 465, 563, 35, 345, 35)
