# analisador de retas para ver se elas formam triângulos

r1 = float(input('Digite comprimento da reta 1:'))
r2 = float(input('Digite o comprimento da reta 2:'))
r3 = float(input('Digite o comprimento da reta 3:'))

if abs(r2-r3) < r1 < r2+r3:
    if abs(r1-r3) < r2 < r1+r3:
        if abs(r1-r2) < r3 < r1+r2:
            print('\033[32msim\n')

            if r1 == r2 and r2 == r3:
                print('É equilátero')
            elif r1 == r2 or r1 == r3 or r2 == r3:
                print('É isoceles')
            else:
                print('é escaleno')

        else:
            print('\033[31m não')
    else:
        print('\033[31m não')
else:
    print('\033[31mnão')
