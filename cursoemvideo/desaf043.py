# índice de massa corporal

p = int(input('Qual o peso da pessoa? (Kg)'))
a = int(input('Qual a altura da pessoa? (cm)'))
imc = p / ((a/100) ** 2)

if imc < 18.5:
    print('Você está ABAIXO DO PESO. Seu IMC é {:.2f}'.format(imc))
elif 18.5 <= imc < 25:
    print('Você está com o peso IDEAL. Seu IMC é {:.2f}'.format(imc))
elif 25 <= imc < 30:
    print('Você está com SOBREPESO. Seu IMC é {:.2f}'.format(imc))
elif 30 <= imc < 40:
    print('Você está com OBESIDADE. Seu IMC é {:.2f}'.format(imc))
else:
    print('Você está com OBESIDADE MÓRBIDA. Seu IMC é {:.2f}'.format(imc))
