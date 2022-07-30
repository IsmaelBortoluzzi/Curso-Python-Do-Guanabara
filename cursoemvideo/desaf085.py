# separando 7 valores entre pares e ímpares v2.0

nums = [[], []]

print('SEPARANDO PARES DE ÍMPARES')

for i in range(7):
    j = int(input(f'Digite o {i+1}° número: '))
    if j % 2 == 0:
        nums[0].append(j)
    elif j % 2 != 0:
        nums[1].append(j)

print(f'Os números pares foram {sorted(nums[0])}')
print(f'Os números ímpares foram os {sorted(nums[1])}')


"""for i in range(7):
    j = int(input(f'Digite o {i+1}° número: '))
    nums.append(j)

print(f'Os números pares digitados foram: ', end=' ')
for c in sorted(nums):
    if c % 2 == 0:
        print(c, end=' ')

print(f'\nOs números ímpares digitados foram:', end=' ')
for c in sorted(nums):
    if c % 2 != 0:
        print(c, end=' ')"""