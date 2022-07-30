# Cadastro de trabalho

from datetime import date

cadastro = dict()

cadastro['Nome'] = str(input('Digite o nome da pessoa: '))
ano_nas = int(input('Digite o ano de nascimento da pessoa: '))
ctps = int(input('Digite o número da carteira de trabalho: (0 se não tem)'))

idade = date.today().year - ano_nas

cadastro['Idade'] = idade
cadastro['CTPS'] = ctps

if ctps == 0:
    print(cadastro['Nome'])
    print(cadastro['Idade'])
else:
    ano_cont = int(input('Digite o ano de contratação: '))
    cadastro['Salário'] = float(input('Digite o salário: '))
    aposen = ano_cont + 35

    cadastro['Ano de contratação'] = ano_cont
    cadastro['Aposentadoria'] = aposen

    print('')
    for k, v in cadastro.items():
        print(f'{k}: {v}', end='')
        print('')
