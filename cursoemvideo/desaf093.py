# Shooter's performance:

desem = dict()
vito = list()

desem['Name'] = str(input('Type the name of the shooter: '))
desem['competitions'] = int(input('How many competiotions did the shooter participate? '))

for i in range(0, desem['competitions']):
    vito.append(int(input(f'How many times the shooter won in the {i+1}° competition? ')))

desem['Wins'] = vito[:]
desem['Score'] = sum(vito)
print('')

for k, v in desem.items():
    print(f'{k}: {v}', end='')
    print('')

print('-='*27)

for i, v in enumerate(vito):
    print(f'In the {i+1}° competition the shooter won {v} times.')