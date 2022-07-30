#Conversor de bases numéricas

r = int(input('Digite um número inteiro:'))

print('[1] converter para BINÁRIO')
print('[2] converter para OCTAL')
print('[3] converter para HEXADECIMAL')

o = int(input('Digite sua opção'))

if o == 1:
    print('O valor em BINÁRIO é:', bin(r)[2:])

elif o == 2:
    print('O valor em OCTAL é:', oct(r)[2:])

elif o == 3:
    print('O valor em HEXADECIMAL é:', hex(r)[2:])

else:
    print('\033[31mNÚMERO INVÁLIDO!!!\033[31m')
