# É primo ou não?

num = int(input('Digite o número a ser analisado:'))

if num == 2 or 1:
    print('O número é primo')
else:
    for c in range(2, num):
        if (num % c) == 0:
            print('O número não é primo')
            break
    else:
        print('O número é primo')
