# DICIONÁRIOS

dados = dict()

"""dados = {'nome': 'pedro', 'idade': 25}
print(dados['nome'])
print(dados['idade'])

dados['sexo'] = 'Masculino'

print(dados)

del dados['idade']

print(dados)"""


"""filme = {'título': 'My Honor Was Loyalty',
         'lançamento': 2016,
         'Diretor': 'Leone Frisa, Alessandro Pepe'
         }

print(filme.values())
print(filme.keys())
print(filme.items())
print('')

for k, v in filme.items():
    print(f'O {k} é {v}')

locadora = list()
print('')
locadora.append(filme)
print(locadora[0]['lançamento'])"""

"""pessoas = {'nome': 'Ismael', 'sexo': 'M', 'idade': 19}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')"""

"""
Uniao = []
estado1 = {'uf': 'Santa Catarina', 'sigla': 'SC'}
estado2 = {'uf': 'Rio Grande do Sul', 'sigla': 'RS'}
estado3 = {'uf': 'Paraná', 'sigla': 'PR'}
Uniao.append(estado1)
Uniao.append(estado2)
Uniao.append(estado3)

print(Uniao[0]['uf'])
"""

estado = dict()
brasil = list()
for i in range(3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla: '))
    brasil.append(estado.copy())
for c in brasil:
    for k, v in c.items():
        print(f'O campo {k} tem valor valor {v}')
print('')

for c in brasil:
    for v in c.values():
        print(v, end=' ')
    print('')
