# Média, maior e menor com WHILE

valor = int(input('Digite o valor: '))
maior = valor
menor = valor
soma = 0
contador = 0

while True:
    soma = soma + valor
    if valor > maior:
        maior = valor
    elif valor < menor:
        menor = valor
    contador = contador + 1
    seguir = str(input('Deseja parar a contagem? (s/n) '.lower()))
    if seguir == 's':
        media = soma / 2
        print('A média entre todos os {} números digitados foi {:.1f}'.format(contador, media))
        print('O maior foi {} e o menor foi {}'.format(maior, menor))
        break
    else:
        valor = int(input('Digite o valor: '))
