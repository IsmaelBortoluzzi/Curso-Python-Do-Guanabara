# Tratando Vários Valores:

print('Digite os valores que quer somar. \n')
print('Digite "999" para parar o programa e ver a soma. \n')

soma = contador = valor = 0

while True:
    valor = int(input('Digite o valor: '))
    if valor - 999 == 0:
        parar = str(input('Deseja parar a contagem? s/n '))
        if parar == 's'.lower():
            break
        else:
            soma += valor
            contador += contador
    else:
        soma = soma + valor
        contador += 1
print(f'A soma dos {contador} valores foi {soma}')
