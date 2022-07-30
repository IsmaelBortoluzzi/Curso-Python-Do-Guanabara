# Alistamento Militar

from datetime import date

a = int(input('Em que ano a pessoa nasceu?'))
h = date.today().year
idade = h-a
alis = (18 - idade) + h

print('Quem nasceu em {} tem {} anos em {}'.format(a, idade, h))

if idade < 18:
    print('Ainda faltam {} anos ({}) para o alistamento.'
          .format(18-idade, alis))
elif idade == 18:
    print('Seu alistamento militar é neste ano.'
          .format(idade))
else:
    print('Seu alistamento militar foi em {}'
          .format(a + 18))
