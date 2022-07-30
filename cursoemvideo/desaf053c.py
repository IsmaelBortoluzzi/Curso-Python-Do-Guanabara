frase = ''.join(str(input('Diga uma frase: ')).split()).lower()

print('A frase digitada foi: {} E o contrário dela é: {}'
      .format(frase, ''.join(reversed(frase))))

if ''.join(reversed(frase)) == frase:
    print('Portanto, ela é um palíndromo!')
else:
    print('Portanto, ela não é um palíndromo.')