# Manipulando o nome de uma pessoa

n = str(input('Digite o seu nome:')).strip()

print(n.upper())
print(n.lower())
print('Seu nome ao todo tem {} letras.'
      .format(len(n.replace(" ", ""))))
#print('Seu primeiro nome tem {} letras'.format(n.find(' ')))

separa = n.split()
print('Seu primeiro nome é {} e tem {} letras.'
      .format(separa[0], len(separa[0])))
