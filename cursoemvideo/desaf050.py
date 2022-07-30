# Soma dos pares

soma = 0
for c in range(1, 6+1):
    w = int(input('Digite o {}° número: '.format(c)))
    if w % 2 == 0:
        soma = soma + w
print('A soma dos números pares desta sequência é: {}'.format(soma))
