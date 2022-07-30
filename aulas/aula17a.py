# LISTAS

lanche = ['hamburguer', 'suco', 'pizza', 'pudin', 'sanduiche',
          'coxinha']
print(lanche)
print(*lanche, sep=', ')  # '*' mostra a lista sem os colchetes, e sep é a string entre as variáveis da lista

"""
lanche[3] = 'sorvete'  # Jeitos de modificar listas
print(lanche)

lanche.append('Bolacha')  # Método para adicionar valores na lista
print(f'{lanche}')

lanche.remove('Bolacha')  # Remove um conteúdo pelo seu nome.
print(lanche)
"""
lanche.insert(-1, 'cachorro quente')  # Método para inserir algo em qualquer posição da lista
print('{}'.format(lanche))
lanche.insert(-2, lanche[-1])
lanche.pop()
print(lanche)
"""
del lanche[3]  # elimina o conteúdo do index 3
print(lanche)

lanche.pop(3)  # elimina o conteúdo do index 3
print(lanche)

lanche.pop()  # elimina o conteúdo do último index da lista
print(lanche)

valores = list(range(4, 12))  # gerando listas com ranges
print(valores)

valores = [9, 2, 4, 0, 6, 4, 7]
print(valores)

valores.sort()  # pondo em ordem a lista
print(valores)

valores.sort(reverse=True)  # pondo a lista em ordem de tras pra frente
print(valores)
"""
"""
a = [1, 9, 4, 7]
b = a  # Vc likou uma lista na outra: se mexer em uma, a outra muda tbm
b[2] = 6
print(f'lista {a}')
print(f'lista {b}')

# Para criar uma cópia sem esta ligação, faça:

a = [1, 9, 4, 7]
b = a[:]
b[2] = 6
print(f'lista {a}')
print(f'lista {b}')"""
