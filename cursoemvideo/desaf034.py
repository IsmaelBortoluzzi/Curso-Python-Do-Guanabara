# aumento múltiplo de salarios

sal = float(input('Digite o salário do escravo:'))

if sal <= 3000:
    ajsal = sal * 0.15
    print('O novo salário do escravo reajustado é: {}'.format(ajsal + sal))

else:
    ajsal = sal * 0.10
    print('O novo salário do escravo reajustado é: {}'.format(ajsal + sal))
