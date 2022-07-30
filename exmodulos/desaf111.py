from ex111.utilidadespy import moeda

j = float(input(f'Digite o valor: '))
g = 29.88
h = 70

print(f'O dobro de {moeda.real(j)} é {moeda.dobro(j, True)}')
print(f'\nA metade de {moeda.real(j)} é {moeda.metade(j, foreal=True)}')
print(f'\nAumetando {float(h):.2f}% de {moeda.real(j)} temos {moeda.aumentar(j, h, True)}')
print(f'\nDiminuindo {float(g):.2f}% de {moeda.real(j)} temos {moeda.diminuir(j, g, foreal=True)}')
