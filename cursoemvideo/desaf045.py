# Pedra, papel, tesoura!

from random import randint
from time import sleep

print('== PEDRA == PAPEL == TESOURA ==')

print('[1] PEDRA')
print('[2] PAPEL')
print('[3] TESOURA')

opcj = int(input('Sua opção:'))
opcc = randint(1, 3)

print('PEDRA...')
sleep(1)
print('PAPEL...')
sleep(1)
print('TESOURA!')

if opcj == 1:
    if opcc == 1:
        print('O jogador jogou PEDRA.')
        print('O computador jogou PEDRA.')
        print('\033[33mEMPATE')
    elif opcc == 2:
        print('O jogador jogou PEDRA.')
        print('O computador jogou PAPEL.')
        print('\033[31mO computador VENCEU!')
    elif opcc == 3:
        print('O jogador jogou PEDRA.')
        print('O computador jogou TESOURA.')
        print('\033[32mO jogador VENCEU!')
elif opcj == 2:
    if opcc == 1:
        print('O jogador jogou PAPEL.')
        print('O computador jogou PEDRA.')
        print('\033[32mO jogador VENCEU!')
    elif opcc == 2:
        print('O jogador jogou PAPEL.')
        print('O computador jogou PAPEL.')
        print('\033[33mEMPATE')
    elif opcc == 3:
        print('O jogador jogou PAPEL.')
        print('O computador jogou TESOURA.')
        print('\033[31mO computador VENCEU!')
elif opcj == 3:
    if opcc == 1:
        print('O jogador jogou TESOURA.')
        print('O computador jogou PEDRA.')
        print('\033[31mO computador VENCEU!')
    elif opcc == 2:
        print('O jogador jogou TESOURA.')
        print('O computador jogou PAPEL')
        print('\033[32mO jogador VENCEU!')
    elif opcc == 3:
        print('O jogador jogou TESOURA.')
        print('O computador jogou TESOURA.')
        print('\033[33mEMPATE')
else:
    print('OPÇÃO INVÁLIDA. Escolha um número entre 1 e 3')
