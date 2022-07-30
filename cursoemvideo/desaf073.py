# Tabela série B

serieb = ('Chapecoense', 'América-MG', 'Cuiabá', 'Juventude',
          'Sampaio Corrêa', 'Ponte Preta', 'Paraná', 'Confiança',
          'CSA', 'Avaí', 'CRB', 'Operário-PR', 'Guarani', 'Brasil de Pelotas',
          'Cruzeiro', 'Vitória', 'Náutico', 'Figueirense', 'Botafogo-SP', 'Oeste')

for i, l in enumerate(serieb):
    print(i+1, l)

print('-='*22)
print('Os 5 primeiros colocados são:')
print('-='*22)

for i, l in enumerate(serieb[0:5]):
    print(i+1, l)

print('-='*22)
print('Os 4 últimos colocados são:')
print('-='*22)

for i, l in enumerate(serieb[-4:]):
    print(i+17, l)

print('-='*22)
print('Os times em ordem alfabética:')
print('-='*22)

for i in sorted(serieb):
    print(i)

print('-='*22)
print('A Chapecoense está na posição: ', end='')

print(serieb.index('Chapecoense')+1)
