# Ordem de precedência dos operadores aritiméticos:
    # 1:  ( )
    # 2:  **
    # 3:  *  /  //  %
    # 4:  +  -

# Dica para encontrar a raiz quadrada de um número:
    # 49**(1/2)
    # raiz cúbica: 343**(1/3)

#  --------------------------//-------------------------

#algo = input('diga algo')
#print('Heil {:~^22}'.format(algo))

# -------------------------//--------------------------

#n1 = int(input('Digite um Valor'))
#n2 = int(input('Digite outro valor'))
#print('O resultado é: {} '.format(n1+n2))

# -------------------------//--------------------------

n1 = int(input('digite um valor'))
n2 = int(input('digite outro valor'))
s = n1+n2
m = n1*n2
d = n1/n2
di = n1//n2
e = n1**n2
print('A soma é {}, o produto é {} e o divisão {:.3f}'.format(s, m, d), end=' ')#este end junta a linha
print('a divisão inteira é {} e \n a potência é {}'.format(di, e)) #este \n quebra a linha
