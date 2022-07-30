# Exercio 83 com falha resolvida vBeta

expressao = input('Digite a expressão: ').strip()
validade = True
tipo_error = ''
quant_parenteses_abrir = expressao.count('(')
quant_parenteses_fechar = expressao.count(')')
parenteses_para_fechar = 0

if quant_parenteses_abrir == quant_parenteses_fechar:
    for v in expressao:
        if v == ')' and parenteses_para_fechar == 0:
            validade = False
            tipo_error = 'Você fechou parentese antes de abrir.'
            break
        if v == '(':
            parenteses_para_fechar += 1
        if v == ')':
            parenteses_para_fechar -= 1
else:
    validade = False
    tipo_error = 'A quantidade de parenteses abrindo é diferente da quantidade de parentese fechando'

if parenteses_para_fechar > 0:
    validade = False
    tipo_error = 'Você esqueceu de fechar um parentese'

if validade is True:
    print(f'A expressão {expressao} está válida!')
else:
    print(f'A expressão {expressao} está errada!')
    print(tipo_error)
