# Programa BUGADO. Só funciona com a gambiarra do 9999999999

print('Cálculo de compra\n')

mais_de_mil = 0
total = 0
preco_prod = 0
menor = 999999999
"""cont = 0"""
mais_bar = ''

while True:
    nome_prod = str(input('Digite o nome do produto: '))
    preco_prod = float(input('Digite o preço do produto: R$'))
    """cont = cont + 1"""
    total = total + preco_prod

    """if cont == 1 or preco_prod < menor:
        menor = preco_prod
        mais_bar = nome_prod"""
    if preco_prod < menor:
        menor = preco_prod
        mais_bar = nome_prod
    if preco_prod > 1000:
        mais_de_mil = mais_de_mil + 1
    cont = str(input('Queres continuar? (S/N) ')).strip().upper()[0]
    while cont not in 'SN ':
        cont = str(input('Queres continuar? (S/N)')).strip().upper()[0]
    if cont == 'N':
        print(f'O total foi R${total:.2f}')
        print(f'{mais_de_mil} produtos custaram mais de 1000 reias')
        print(f'O produto mais barato foi o {mais_bar}')
        break
    else:
        continue
print('{:-^40}'.format(' FIM DO PROGRAMA '))