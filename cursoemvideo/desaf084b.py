# Lista composta de análise de dados

listam = list()
listam2 = list()
maior = menor = 0

print('-=-=-=- Análise de pessoas -=-=-=-')

while True:
    listam.append(str(input('\nNome: ')))
    listam.append(float(input('Peso: ')))
    con = str(input('\nDeseja continuar? (S/N)')).upper().strip()
    if con == 'N':
        print('\nSaindo do programa...\n')
        break

for g in listam:
    if type(g) == int or type(g) == float:
        listam2.append(g)

maior = max(listam2)
menor = min(listam2)

print(f'A quantidade de pessoas cadastrada foram {len(listam2)}\n')
print(f'A(s) pessoa(s) mais pesada(s) foi/foram '
      f'{listam[listam.index(maior) - 1]}, com {listam[listam.index(maior)]}\n')
print(f'A(s) pessoa(s) mais leves(s) foi/foram '
      f'{listam[listam.index(menor) - 1]}, com {listam[listam.index(menor)]}\n')
