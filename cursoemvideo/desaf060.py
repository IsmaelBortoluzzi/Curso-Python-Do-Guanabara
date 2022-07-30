# Cálculo de Fatorial:

n = int(input('Digite um valor para saber seu fatorial: '))
contador = n

while contador != 1:
    print('{}'.format(contador), end='')
    print(' x ' if contador > 2 else ' = ', end='')
    contador = contador - 1
    n = (contador * n)
print(n)

print('\n')

valor = int(input('Digite o valor a receber o cálculo fatorial: '))
contador = valor

for _ in range(valor - 1, 0, -1):
    contador = contador - 1
    valor = contador * valor
print(valor)
