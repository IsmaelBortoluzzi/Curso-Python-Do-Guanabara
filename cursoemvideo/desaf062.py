# PA v2.0

print('calculadora de PA \n')

pri_val = int(input('Digite o primeiro valor da PA: '))
razao = int(input('Digite a razão da PA: '))
ult_termo = int(input('Digite o último termo da PA:'))
formula = pri_val + (ult_termo - 2) * razao

print(pri_val, end=' ')

while pri_val <= formula:
    pri_val = pri_val + razao
    print(pri_val, end=' ')

while True:
    print('\n')
    cont = str(input('Queres continuar?'))
    print('\n')
    if cont == 'sim' or 's':
        pri_val = int(input('Digite o primeiro valor da PA: '))
        razao = int(input('Digite a razão da PA: '))
        ult_termo = int(input('Digite o último termo da PA:'))
        formula = pri_val + (ult_termo - 2) * razao

        print(pri_val, end=' ')

        while pri_val <= formula:
            pri_val = pri_val + razao
            print(pri_val, end=' ')
    else:
        print('Obrigado pela preferência!')
        break
