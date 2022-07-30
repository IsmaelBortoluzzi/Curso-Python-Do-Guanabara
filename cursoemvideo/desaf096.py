# Área de terrenos com funções:

print('CONTROLE DE TERRENOS')
print('----------------------')


def area(l, c):
    print(f'A área de um terreno {l}x{c} é {l*c:.2f}m²')


lar = float(input('Largura: (m) '))
com = float(input('Comprimento: (m) '))
print('')
area(lar, com)
