# Sequência de Fibonacci

print('Sequência de Fibonacci \n')
limite = int(input('Quantos caracteres quer a sequência? '))
contador = 0
f1 = 0
f2 = 2
f3 = 1

if limite == 1:
    print('0')
elif limite == 2:
    print('0 1')
elif limite == 3:
    print('0 1 1')
elif limite == 4:
    print('0 1 1 2')
else:
    print('0 1 1 2', end=' ')
    while contador != limite - 4:
        f1 = f2 + f3
        if f2 < f3:
            f2 = f1
        elif f3 < f2:
            f3 = f1
        contador = contador + 1
        print(f1, end=' ')
