# Dicionário simples em python

situa = dict()

situa['aluno'] = str(input('Digite do aluno: '))
situa['media'] = float(input('Digite a média do aluno: '))

if situa['media'] >= 7:
    situa['situação'] = '\033[32mAPROVADO \033[m'
elif 7 > situa['media'] >= 5:
    situa['situação'] = '\033[33mRECUPERAÇÃO \033[m'
else:
    situa['situação'] = '\033[31mREPROVADO \033[m'

print(f'O aluno {situa["aluno"]}, cuja média é ', end='')
print(f"{situa['media']}, está {situa['situação']}")

