# Cálculo de desconto

preco = float(input('Insira o preço do produto(R$):'))
des = float(input('Insira a porcentagem de desconto em decimal'
                  '(ex: 10% = 0.10)'))
vf = preco-(preco*des)

print('O produto custará {:.2f}R$ com o desconto de {}%'
      .format(vf, des*100))