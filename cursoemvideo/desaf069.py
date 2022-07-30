# Análise de dados do grupo

print('Cadastro de Pessoas\n')

hom = mul_sub_20 = de_maior = contador = 0

while True:
    # nome = str(input('Digite o nome da pessoa: '))
    sexo = ' '
    while sexo not in 'mf':
        sexo = str(input('Qual o sexo da pessoa? (masculino/feminino) ')).strip().lower()[0]
    idade = int(input('Qual a idade da pessoa? '))

    if sexo == 'm':
        hom = hom + 1
    if sexo == 'f' and idade < 20:
        mul_sub_20 = mul_sub_20 + 1
    if idade >= 18:
        de_maior = de_maior + 1
    contador = contador + 1

    cont = str(input('Deseja inserir mais pessoas para a análise? (s/n) '))
    if cont == 'n'.lower():
        print(f'De todas as {contador} pessoas analisadas, {hom} são homens, '
              f'{mul_sub_20} são mulheres com menos de 20 anos e '
              f'{de_maior} são pessoas maior de idade.')
        break
    else:
        continue
