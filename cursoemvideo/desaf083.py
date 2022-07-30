# Verificador de expressões matemáticas:

print('VALIDADOR DE FÓRMULAS MATEMÁTICAS')

while True:
    f = str(input('\nDigite a fórmula matemática: ')).split()
    for c in f:
        for i in c:
            if c.count('(') == c.count(')'):
                print(f'\nA fórmula {c} \033[36mdará\033[m certo.')
                break
            elif c.count('(') != c.count(')'):
                print(f'\nA fórmula {c} \033[31mnão dará\033[m certo')
                break
    j = str(input('\nDeseja testar outra fórmula: (S/N)')).upper().strip()
    if j == 'N':
        print('\nEncerrando...')
        break
