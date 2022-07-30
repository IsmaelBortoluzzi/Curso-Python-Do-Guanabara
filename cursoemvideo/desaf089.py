# Boletim com listas compostas.

from time import sleep

print('=-=-=-=- SISTEMA DE NOTAS -=-=-=-=-')

listas = []
alunos = []
notas = []

while True:
    alun = str(input('\nDigite o nome do aluno: '))
    alunos.append(alun)

    nota1 = float(input('Digite a 1° nota: '))
    notas.append(nota1)

    nota2 = float(input('Digite a 2° nota: '))
    notas.append(nota2)

    alunos.append(notas[:])
    listas.append(alunos[:])
    alunos.clear()
    notas.clear()

    cont = str(input('\nQuer contiuar? (S/N)')).strip().upper()
    if cont == 'N':
        break
print('')

pos1 = 0
for i in listas:
    print(pos1, end=' ')
    print(f'A média do(a) {listas[pos1][0]} é:   ', end='')
    print(f'{(i[1][0] + i[1][1]) / 2}')
    pos1 += 1
    sleep(0.70)
while True:
    j = int(input('\nDigite o código do aluno que queres: (999 para sair)'))
    if j == 999:
        break
    if j > len(listas)-1:
        print('\nEste aluno não existe tente novamente!')
    else:
        print(f'\nAs notas do(a) {listas[j][0]} são: {listas[j][1]}')
