# Lista composta de análise de dados vMelhorada

pessoas = []
lista = list()
maior = menor = 0

print('-=-=-=- Análise de pessoas -=-=-=-')

while True:
    lista.append(str(input('\nNome: ')))
    lista.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maior = menor = lista[1]
    else:
        if lista[1] > maior:
            maior = lista[1]
        elif lista[1] < menor:
            menor = lista[1]
    pessoas.append(lista[:])
    lista.clear()
    con = str(input('\nDeseja continuar? (S/N)')).upper().strip()
    if con == 'N':
        print('\nSaindo do programa...\n')
        break

print(f'A quantidade de pessoas cadastrada foram {len(pessoas)}\n')

print(f'A(s) pessoa(s) mais pesada(s) foi/foram', end=' ')
for i in pessoas:
    if i[1] == maior:
        print(i[0], end=' ')

print(f'\nA(s) pessoa(s) mais leves(s) foi/foram', end=' ')
for c in pessoas:
    if c[1] == menor:
        print(c[0], end=' ')
