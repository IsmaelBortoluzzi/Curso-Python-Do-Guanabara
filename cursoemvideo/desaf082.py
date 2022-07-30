# Dividindo valores em uma lista

print('Iniciando Contador...\n')
print('Digite "\033[36m999\033[m" para sair do programa\n')

lista = list()
listapar = list()
listaimpar = list()

while True:
    lista.append(int(input('Digite um número: ')))
    if lista[-1] == 999:
        j = str(input('\nDeseja realmente sair do programa? (S/N)\n')).upper().strip()
        if j == 'S':
            lista.pop()
            break
for i in lista:
    if i % 2 == 0:
        listapar.append(i)
    else:
        listaimpar.append(i)
print(f'\nSua lista ficou com estes valores: \033[34m{lista}\033[m')
print(f'Os números pares desta lista compreendem \033[32m{listapar}\033[m')
print(f'Os números ímpares desta lista compreendem \033[31m{listaimpar}\033[m')
