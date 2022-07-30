# Atualização com a função real() imbutida direto nas outras funções

from ex109 import ex109moeda

j = float(input(f'Digite o valor: '))
g = 29.88
h = 70

print(f'O dobro de {ex109moeda.real(j)} é {ex109moeda.dobro(j, False)}')
print(f'\nA metade de {ex109moeda.real(j)} é {ex109moeda.metade(j, foreal=True)}')
print(f'\nAumetando {float(h):.2f}% de {ex109moeda.real(j)} temos {ex109moeda.aumentar(j, h, True)}')
print(f'\nDiminuindo {float(g):.2f}% de {ex109moeda.real(j)} temos {ex109moeda.diminuir(j, g, foreal=False):.2f}')