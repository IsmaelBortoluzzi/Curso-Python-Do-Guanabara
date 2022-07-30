# Calculadora de salários N°2

si = float(input('Digite o salário: R$'))
a = int(input('Insira a porcentagem de aumento:'))
sf = si + (si * a / 100)
print('O novo salário do funcionário derá de: R${:.2f}'
      .format(sf))

