# Função leiaint() e leiafloat()

from ex111.utilidadespy import moeda, dado

inte = dado.leiaint('Digite um número inteiro: ')
print(inte)

real = dado.leiafloat('Digite um número real: ')
print(f'{real:.2f}')
