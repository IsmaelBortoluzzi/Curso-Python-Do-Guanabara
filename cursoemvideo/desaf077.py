# Apontando vogais em uma palavra de uma tupla

wor = ('onça', 'leopardo', 'tigre', 'leopardo das neves',
       'leao', 'cachorro', 'gato', 'puma', 'black-footed cat',
       'gato do deserto', 'caracal', 'linx', 'jaguatirica')

for i in wor:
    pala = f'Na palavra {i.upper()} tem as vogais: '
    if (i.find('a')) != -1:
        pala = pala + ' A '
    if (i.find('e')) != -1:
        pala = pala + ' E '
    if (i.find('i')) != -1:
        pala = pala + ' I '
    if (i.find('o')) != -1:
        pala = pala + ' O '
    if (i.find('u')) != -1:
        pala = pala + ' U '
    print(pala)
