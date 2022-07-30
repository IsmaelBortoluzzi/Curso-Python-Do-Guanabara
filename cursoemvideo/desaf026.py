n = str(input('Digite algo:')).lower().strip()

print('A letra "A" aparece {} na frase.'.format((n.count('a'))))
print('A 1° letra A aparece na posição {}'.format(n.find('a')+1))
print('A última letra A aparece na posição {}'.format(n.rfind('a')+1))
