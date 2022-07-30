# Maior e menor número v Guanabara

listanum = []
maior = 0
menor = 0

for c in range(5):
    listanum.append(int(input(f'Digite o {c+1}° número: ')))
    if c == 0:
        maior = menor = listanum[c]
    else:
        if listanum[c] > maior:
            maior = listanum[c]
        if listanum[c] < menor:
            menor = listanum[c]
print('-='*30)
print(f'Você digitou os valores {listanum}')
print(f'O maior valor digitado foi o {maior}, na posição', end='')
for i, v in enumerate(listanum):
    if v == maior:
        print(f' {i}...', end='')
print(f'\nO menor valor digitado foi o {menor}, na posição', end='')
for i, v in enumerate(listanum):
    if v == menor:
        print(f' {i}...', end='')