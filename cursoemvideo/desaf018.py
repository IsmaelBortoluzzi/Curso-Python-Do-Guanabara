# Calcula valores de sen, cos e tan de um angulo

import math

a1 = float(input('Insira o valor um ângulo:'))
seno = (math.sin(math.radians(a1)))
coss = math.cos(math.radians(a1))
tang = math.tan(math.radians(a1))
print('O seno de {} é {:.2f}, seu cosseno é {:.2f} e sua tangente é {:.2f}'.format(a1, seno, coss, tang))