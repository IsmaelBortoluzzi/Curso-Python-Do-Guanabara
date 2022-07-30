# Jogo de Par ou Impar

from random import randint

print('-'*20)
print('JOGO DO PAR OU ÍMPAR')
print('-'*20)

contador = 0

while True:
    esc = ' '
    while esc not in 'pií':
        esc = str(input('Par ou Ímpar? ')).strip().lower()[0]
    valor = int(input('Digite um número para jogar de 1 a 100: '))
    c = randint(1, 100)

    if esc == 'p':
        if (valor + c) % 2 == 0:
            print(f'\nA máquina jogou {c} e o jogadou jogou {valor}')
            print(f'\n{c} + {valor} = {c + valor}')
            print('\n\033[32mVocê venceu!\033[m\n')
            contador += 1
        elif (valor + c) % 2 != 0:
            print(f'\nA máquina jogou {c} e o jogador jogou {valor}')
            print(f'\n{c} + {valor} = {c + valor}')
            print('\n\033[31mO computador venceu!\033[m\n')
            print(f'De todas as {contador + 1} partidas jogadas, você ganhou {contador} partidas.')
            break
    elif esc == 'i' or 'í':
        if (valor + c) % 2 != 0:
            print(f'\nA máquina jogou {c} e o jogador jogou {valor}')
            print(f'\n{c} + {valor} = {c + valor}')
            print('\n\033[32mVocê venceu!\033[m\n')
            contador += 1
        elif (valor + c) % 2 == 0:
            print(f'\nA máquina jogou {c} e o jogador jogou {valor}')
            print(f'\n{c} + {valor} = {c + valor}')
            print('\n\033[31mO computador venceu!\033[m\n')
            print(f'De todas as {contador + 1} partidas jogadas, você ganhou {contador} partidas.')
            break
