# Conversor de cm para mm, m, pol, pés e jar

cc = float(input('digite um valor em centímetros:'))
print('{}cm = {:.2f}mm'.format(cc, cc*10))
print('{}cm = {:.2f}m'.format(cc, cc/100))
print('{}cm = {:.2f} pol'.format(cc, cc/2.54))
print('{}cm = {:.2f}pés'.format(cc, cc/30.48))
print('{}cm = {:.2f}jar'.format(cc, cc/91.44))

