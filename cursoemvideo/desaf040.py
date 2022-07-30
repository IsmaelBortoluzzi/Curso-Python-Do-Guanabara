# Nota melhorada

n1 = int(input('Digite a primeira nota do aluno:'))
n2 = int(input('Digite a segunda nota do aluno:'))
n3 = int(input('Digite a terceira nota do aluno:'))
media = (n1 + n2 + n3) / 3

if media >= 7:
    print('A média do aluno foi {:.2f}'.format(media))
    print('O aluno está \033[32mAPROVADO\033[m')
elif 7 > media >= 5:
    print('A média do aluno foi {:.2f}'.format(media))
    print('O aluno está em \033[33mRECUPERAÇÃO\033[m')
else:
    print('A média do aluno foi {:.2f}'.format(media))
    print('O aluno está \033[31mREPROVADO\033[m')
