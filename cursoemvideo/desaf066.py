# Somando vários valores com um flag de parada

soma = contador = 0

while True:
    valor = int(input('Digite o valor (999 para parar): '))
    if valor == 999:
        print(f'A soma dos {contador} valores foi {soma}')
        break
    contador = contador + 1
    soma = soma + valor
