# Extraindo dados de uma lista

lista = list()

print('Digite "999" para sair do programa')

while True:
    lista.append(int(input('Digite o número para por na lista: ')))
    if lista[-1] == 999:
        c = str(input('Tem certeza que deseja parar o programa? (S/N) ')).strip().split()
        if c == 'S':
            lista.pop()
            break
print(lista)
print(f'\nFora digitados {len(lista)} valores.')
print(f'\nA lista ordenada de forma decrescente é {lista.sort(reverse=True)}.')
if lista.count(5) != 0:
    print(f'O número 5 foi digitado na lista {lista.count(5)} vez(es)')
else:
    print('O número 5 não aparece na lista')
