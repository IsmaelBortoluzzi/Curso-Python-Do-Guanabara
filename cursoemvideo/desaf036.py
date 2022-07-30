# calcular financiamento para compra de casa

valor = float(input('Insira o valor da casa:'))
sal = float(input('Insira o salário da pessoa:'))
prazo = int(input('Insira (em meses) o prazo que a pessoa vai pagar:'))
prestacao = valor / prazo

if sal * 0.30 >= prestacao:
    print('O financiamento será \033[32mliberado! \033[m')
    print('O valor da prestação será de R${:.2f}'.format(prestacao))
else:
    print('O financiamento está \033[31mnegado! \033[m')
    print('O valor da prestação será de R${:.2f}'.format(prestacao))
