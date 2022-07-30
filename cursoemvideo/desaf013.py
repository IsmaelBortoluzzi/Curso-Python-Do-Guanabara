# Cauculadora de aumentos salariais

sa = float(input('Digite o salário do funcionário(R$):'))
a = float(input('Digite a porcentagem de aumento em decimal:'
                ' (ex: 10% = 0.10)'))
sf = sa + (sa*a)
print('O salário subirá de {:.2f} para {:.2f}'.format(sa, sf))
