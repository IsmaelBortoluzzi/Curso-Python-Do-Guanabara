# Criando um menu de opções:

valor1 = int(input('Digite o primero número: '))
valor2 = int(input('Digite o segundo número: '))

while True:
    print('[1] Soma')
    print('[2] Multiplicação')
    print('[3] Maior')
    print('[4] Novos Números')
    print('[5] Sair Do Programa')

    opcao = int(input('Qual sua opção? '))

    if opcao == 1:
        print('A RESPOSTA É: {}'.format(valor1 + valor2))
        continue
    elif opcao == 2:
        print('A RESPOTA É: {}'.format(valor1 * valor2))
        continue
    elif opcao == 3:
        if valor1 > valor2:
            print('O PRIMEIRO valor é MAIOR do que o segundo.')
        elif valor1 < valor2:
            print('O SEGUNDO valor é MAIOR do que o primeiro.')
        else:
            print('Ambos os valores são iguais.')
        continue
    elif opcao == 4:
        valor1 = int(input('Digite o primero número: '))
        valor2 = int(input('Digite o segundo número: '))
    elif opcao == 5:
        break
    else:
        print('Opção inválida! Por favor, tente novamente.')
        valor1 = int(input('Digite o primero número: '))
        valor2 = int(input('Digite o segundo número: '))
