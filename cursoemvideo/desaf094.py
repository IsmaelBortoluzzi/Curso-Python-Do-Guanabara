# unindo dicionários e listas:

print('Cadastro de pessoas: (Digite "Parar" no campo "Nome" para parar.)')

cad = dict()
bdd = []

while True:
    print('')
    cad['Nome'] = str(input('Nome: ')).title()
    if cad['Nome'] == 'Parar':
        break
    cad['Sexo'] = str(input('Sexo: (M/F)')).strip().upper()
    cad['Idade'] = int(input('idade: '))

    if cad['Nome'] == 'Parar'.strip():
        break
    if cad['Sexo'] not in 'MF' or cad['Idade'] > 130:
        print('Dados inválidos. Tente novamente.')
        continue
    else:
        bdd.append(cad.copy())
        cad.clear()

print('-='*25)

print(f'A quantidade de pessoas cadastradas foi {len(bdd)}')

media = 0
qnt_hom = 0
qnt_mul = 0
mul = list()

for i in bdd:
    for v in i.values():
        if type(v) == int:
            media += v
        media = media / 2
    for k in i.keys():
        if k == 'Sexo':
            if i['Sexo'] == 'F':
                mul.append(i)
                qnt_mul += 1
            if i['Sexo'] == 'M':
                qnt_hom += 1

print(f'\nAs mulheres cadastradas foram: ')
for m in mul:
    print(f'{m["Nome"]}')
print(f'\nA quantidade de homens cadastrados foi {qnt_hom}')
print(f'A quantidade de mulheres cadastradas foi {qnt_mul}')
print(f'\nA média de idade das pessoas cadastradas foi de {media:.2f} anos.')

aci_med = list()
for i in bdd:
    for k in i.keys():
        if k == 'Idade':
            if i['Idade'] > media:
                aci_med.append(i)
print('\nAs pessoas acima da média de idade são: ')
for n in aci_med:
    print(f"{n['Nome']} com {n['Idade']} anos", end='')
    print('')
