# Apontando vogais em uma palavra de uma tupla v2.0

wor = ('onça', 'leopardo', 'tigre', 'leopardo das neves',
       'leao', 'cachorro', 'gato', 'puma', 'black-footed cat',
       'gato do deserto', 'caracal', 'linx', 'jaguatirica')

for palavras in wor:
    print(f'\nNa palavra {palavras.upper()} temos: ', end='')
    for letra in palavras:  # cada palavra também é uma tupla de letras
        if letra.lower() in 'aeiou':
            print(letra.upper(), end=' ')
