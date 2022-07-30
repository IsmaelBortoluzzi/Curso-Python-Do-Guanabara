# Programa principal

# from ex107 import ex107moeda

from ex108 import ex108moeda
# Atualização com a função real()

j = float(input(f'Digite o valor: '))
g = 29.88
h = 70

print(f'O dobro de {ex108moeda.real(j)} é {ex108moeda.real(ex108moeda.dobro(j))}')
print(f'\nA metade de {ex108moeda.real(j)} é {ex108moeda.real(ex108moeda.metade(j))}')
print(f'\nAumetando {ex108moeda.real(h)}% de {ex108moeda.real(j)} temos {ex108moeda.real(ex108moeda.aumentar(j, h))}')
print(f'\nDiminuindo {ex108moeda.real(g)}% de {ex108moeda.real(j)} temos {ex108moeda.real(ex108moeda.diminuir(j, g))}')

