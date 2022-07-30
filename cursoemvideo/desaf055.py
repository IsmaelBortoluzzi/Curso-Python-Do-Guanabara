# Maior e menor peso

peso_a = float(input('Digite o peso da 1° pessoa:'))
maior = peso_a
menor = peso_a

for i in range(2, 5+1):
    peso = float(input('Digite o peso da {}° pessoa:'.format(i)))
    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
print('A pessoa mais pesada pesa {:.2f}kg e a mais leve pesa {}kg'
      .format(maior, menor))
