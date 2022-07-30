# Sequência de Fibonacci v2.0

print('Sequência de Fibonacci v2.0 \n')

limite = int(input('quantos caracteres quer a sequência? '))
f1 = contador = 0
f2 = 1
f3 = 2

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
    while contador < limite - 4:
        f1 = f2 + f3
        if f2 < f3:
            f2 = f1
        elif f3 < f2:
            f3 = f1
        contador += 1
        print(f1, end=' ')
