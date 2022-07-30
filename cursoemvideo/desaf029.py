v = float(input('velocidade'))

if v > 80:
    multa = (v - 80) * 7
    print('Você ultrapassou o limite de velocidade (80km/h)!')
    print('Você está trafegando a {}km/h'.format(v))
    print('Sua multa a pagar é de R${}'.format(multa))
else:
    print('Boa viagem!')