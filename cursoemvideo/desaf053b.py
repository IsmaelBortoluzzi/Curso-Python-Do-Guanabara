f = str(input('Digite frase')).upper().replace('', ' ')
inverso = ''
for letra in range(len(f) -1, -1, -1):
    inverso = inverso + f[letra]

if inverso == f:
    print('É um palíndromo')
else:
    print('Não é um palindromo')