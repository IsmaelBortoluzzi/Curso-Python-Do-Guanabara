# Tabuada 3.0

while True:
    valor = int(input('\nDigite o valor da tabuada: '))
    contador = 0

    while contador <= 10:
        resul = valor * contador
        print(f'{valor} x {contador} = {resul}')
        contador += 1

    repetir = str(input('\nDeseja calcular a tabuada de mais um número? (s/n) '))
    if repetir == 'n'.lower():
        print('\nTabuada encerrando. Volte sempre!')
        break
