# Maior e menor valor com listas

valores = list()

for i in range(5):
    valores.append(int(input(f'Digite o {i+1}° valor aleatório: ')))

maior = valores.index(max(valores))
menor = valores.index(min(valores))
a = f'O maior valor digitado foi o {max(valores)} na posição'
b = f'O menor valor digitado foi o {min(valores)} na posição'
for _ in valores:
    if _ == max(valores):
        a += f' {valores.index(_, maior) + 1}...'
        maior += 1
    if _ == min(valores):
        b += f' {valores.index(_, menor) + 1}...'
        menor += 1
print(a)
print(b)
