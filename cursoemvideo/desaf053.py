# Identificando Palindromos(?):

f = str(input('Digite a frase a ser analisada:')).lower().replace(' ', '')

if f == f[::-1]:
    print('É um palindromo.')
else:
    print('Não é um palindromo.')
