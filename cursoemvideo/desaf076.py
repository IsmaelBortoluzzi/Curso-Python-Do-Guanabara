# Lista de preço com tuplas

print('-'*40)
print('LISTAGEM DE PREÇOS')
print('-'*40, '')


guns = ('HK 4', 922.59, 'Glock 20', 509.12, 'Walther PPQ', 564.98,
        'CZ 75b', 573.88, 'SIG P365', 599.99, 'CZ Shadow 2', 1998.99,
        'KORTH PRS', 5798.98, 'Glock 19', 505.93, 'USP 45 T', 999.99,
        'CZ P01', 639.94, 'Walther PPK', 799.99, 'USP 9', 989.90,
        'HK P30', 709.97, 'HK P7', 1590.99, 'Glock 43', 505.93,
        'MK 23', 2000.01, 'M9A3', 1000.99, 'Glock 43x', 480.33,
        'Glock 48', 540.95, 'M1911 A1', 600.54)

for i in guns:
    if type(i) == str:
        print('{:.<30}'.format(i), end='')
    elif type(i) == float:
        print('US$', i, '')

print('-'*40)

print('{:-^40}'.format(' FIM DO PROGRAMA '))
