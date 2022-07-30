# Gerenciamento de pagamentos

print('{:=^42}'.format(' LOJÃO DO ALEMÃO '))

p = float(input('Qual o preço das compras? (R$)'))

print('FORMAS DE PAGAMENTO')

print('[1] Pagamento à vista em dinheiro/cheque')
print('[2] Pagamento à vista no cartão')
print('[3] Pagamento em 2x no cartão')
print('[4] Pagamento em 3x ou mais no cartão')

o = int(input('Qual sua escolha:'))

if o == 1:
    print('Sua compra custará agora R$\033[32m{:.2f}\033[m com o desconto'
          .format(p - (p * 0.10)))
elif o == 2:
    print('Sua compra custará agora R$\033[32m{:.2f}\033[m com o desconto'
          .format(p - (p * 0.05)))
elif o == 3:
    print('Sua compra custará R$\033[32m{:.2f}\033[m e terá 2 parcelas de '
          'R$\033[32m{:.2f}\033[m'.format(p, p / 2))
elif o == 4:
    a = int(input('Quantas vezes será parcelada a compra?'))
    print('A compra parcelada em \033[32m{}\033[mx, custará no fim R$\033[32m{:.2f}\033[m'
          ' e terá parcelas no valor de R$\033[32m{:.2f}\033[m'
          .format(a, p + (p * 0.20), (p + (p * 0.20)) / a))
else:
    print('Código INVÁLIDO. O código das formas de pagamentos são entre 1 e 4!')