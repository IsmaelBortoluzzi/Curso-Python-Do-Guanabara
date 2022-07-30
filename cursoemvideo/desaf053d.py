"""carro = ['porsche', 'ferrari', 'lamborghini', 'BMW', 'Audi']
ordem_preço = ['1°', '2°', '3°', '4°', '5°']

carro_preço = tuple(zip(carro, ordem_preço))

for a, b in carro_preço:
    print('O veículo {} é o {} mais caro'.format(a, b))"""

g = str(input('Digite algo'))
i = 0
pal = ''
for letra in g:
    pal += letra
    i += 1
    if i > 2:
        print(pal)
        pal = ''
        i = 0
else:
    print(pal)


