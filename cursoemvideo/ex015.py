# Aluguel de carros

d = int(input('Por quantos dias o carro ficou alugado?'))
km = float(input('Quantos quilômetros foram rodados com o carro?'))
vf = (d * 60) + (km * 0.15)
print('O total a ser pago será de R${:.2f}'.format(vf))