# Desafio 083 vGuanabara

exp = str(input('Digite uma expressão: '))
pilha = []

for sim in pilha:
    if exp == '(':
        pilha.append('(')
    elif exp == ')':
        if len(pilha) > 0:
            pilha.pop(0)
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão deu certo!')
else:
    print('Sua expressão não deu certo!')
