# Oprimindo feministas

sexo = ''

while sexo not in 'MASCULINO' or 'FEMININO':
    sexo = str(input('Qual o sexo da pessoa? ')).upper()
    if sexo == 'MASCULINO':
        print('Cuzão')
        break
    elif sexo == 'FEMININO':
        print('Goztoza')
        break
    else:
        print('NÃO EXISTEM MÚLTIPLOS GÊNEROS, IMBECIL!!!')
