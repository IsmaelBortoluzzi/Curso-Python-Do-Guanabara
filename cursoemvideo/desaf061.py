# PA v2.0

print('calculadora de PA \n')

pri_val = int(input('Digite o primeiro valor da PA: '))
razao = int(input('Digite a razão da PA: '))
formula = pri_val + (9-1) * razao

print(pri_val, end=' ')

while pri_val <= formula:
    pri_val = pri_val + razao
    print(pri_val, end=' ')
