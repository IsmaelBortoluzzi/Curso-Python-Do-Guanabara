# Análise de dados em uma tupla

nums = ()
cont = 0

for i in range(4):
    nums += (int(input(f'Digite o {i+1}° número: ')),)

print(f'O número 9 apareceu {nums.count(9)} vez(es).')

if 3 not in nums:
    print('O número 3 não aparece em nenhuma posição.')
else:
    print(f'O primeiro 3 aparece na posição {nums.index(3) + 1}')

for i in nums:
    if i % 2 == 0:
        cont += 1
print(f'Números pares apareceram {cont} vez(es)')
