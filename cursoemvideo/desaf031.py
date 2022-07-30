# custo da viagem

d = float(input('Digite a distância da viagem:'))

if d <= 200:
    to = d * 0.75
    print('A viagem custará R${:.2f}'.format(to))
else:
    to = (200 * 0.75) + (d - 200) * 1
    print('A viagem custará R${:.2f}'.format(to))