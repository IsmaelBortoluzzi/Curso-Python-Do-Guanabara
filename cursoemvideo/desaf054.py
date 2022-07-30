# Quem já atingiu a maioridade?

from datetime import date

hoje = date.today().year
maior = 0
menor = 0

for g in range(1, 7+1):
    nascim = int(input('Digite o ano de naciemnto da {}° pessoa:'.format(g)))
    if hoje - nascim < 18:
        menor += 1
    elif hoje - nascim >= 18:
        maior += 1
print('Existem {} menores de idade e {} maiores.'
      .format(menor, maior))
