# Cálculo de quantidade de tinta a ser usada

al = float(input('Insira a altura da parede (m):'))
l = float(input('Insira a largura da parede (m):'))
area = al*l
print('A quantidade de tinta necessária para pintar a parede '
      'será: {:.2f}L'.format(area/2))



