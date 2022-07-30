# analisador de retas para ver se elas formam triângulos v2.0

r1 = float(input('1 reta:'))
r2 = float(input('2 reta:'))
r3 = float(input('3 reta:'))

if r1 < r2+r3 and r2 < r1+r3 and r3 < r1+r2:
    if r1+r2+r3 == r1*3:
        print('O triângulo é EQUILÁTERO')
    elif r1+r2 == r1*2 or r1+r3 == r3*2 or r2+r3 == r2*2:
        print('O triângulo é ISÓCELES')
    else:
        print('O triângulo é ESCALENO')
else:
    print('Não é possível a formação de um triângulo.')
