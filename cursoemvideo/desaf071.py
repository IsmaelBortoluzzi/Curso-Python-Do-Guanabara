# Banco ROBONESTO

print('='*20)
print('Banco ROBONESTO')
print('='*20)

valor = int(input('Digite o valor que deseja sacar: R$'))
n50 = valor // 50

while True:
    if n50 != 0:
        print(f'Foram sacadas {n50} notas de R$50,00')
        valor = valor - (n50 * 50)
    n20 = valor // 20
    if n20 != 0:
        print(f'Foram sacadas {n20} notas de R$20,00')
        valor = valor - (n20 * 20)
    n10 = valor // 10
    if n10 != 0:
        print(f'Foram sacadas {n10} notas de R$10,00')
        valor = valor - (n10 * 10)
    n1 = valor // 1
    if n1 != 0:
        print(f'Foram sacadas {n1} notas de R$1,00')
    break
print('='*20)
print('Volte e sempre ao Banco ROBONESTO!')
print('='*20)
