# Valores únicos em uma lista

print('-='*19)
print('Iniciando registrador de cadastros...')
print('\nDigite "999" para sair do programa.')
print('-='*19)

cadastro = list()

while True:
    cadastro.append(int(input('Digite o número do cadastro: ')))
    if cadastro[-1] == 999:
        parar = str(input('Quer parar a contagem? ')).strip().upper()
        if parar == 'S':
            cadastro.pop()
            break
    if cadastro.count(cadastro[-1]) != 1:
        cadastro.pop()
        print('Valor repetido. Tente novamente!')
    else:
        print(f'Valor {cadastro[-1]} inserido com sucesso!')

print('-='*19)

print(f'Os cadastros digitados foram: ', end='')
for i in sorted(cadastro):
    print(i, end=' ')
