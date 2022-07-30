# Classificando Atletas

from datetime import date

a = int(input('Digite o ano de nascimento do atleta:'))
h = date.today().year
i = h - a

print('O atleta tem {} anos de idade'.format(i))
if i <= 9:
    print('O atleta é classificado como MIRIM')
elif 9 < i <= 14:
    print('O atleta é classificado como INFANTIL')
elif 14 < i <= 19:
    print('O altleta é classificado como JÚNIOR')
elif 19 < i <= 25:
    print('O atleta é classificado como SÊNIOR')
else:
    print('O atleta é classificado como MASTER')
