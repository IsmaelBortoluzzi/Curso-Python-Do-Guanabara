# Cálculo de desconto N°2

vi = float(input('Informe o preço do produto: R$'))
d = int(input('Informe a porcentagem do desconto:'))
pd = (d/100 * vi)
vf = (vi - pd)
print('O pruduto com {}% de desconto custará R${:.2f}'
      .format(d, vf))