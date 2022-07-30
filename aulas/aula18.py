# LISTAS (PARTE 2)

"""
pessoas = [['Pedro', 32], ['Maria', 28], ['João', 34]]

print(pessoas[0][0])
print(pessoas[1][0])
print(pessoas[2][1])
"""

"""
teste = list()
teste.append('Ismael')
teste.append(19)
print(teste)
garela = list()
garela.append(teste[:])
teste[0] = 'Maria'
teste[1] = 18
garela.append(teste[:])
print(garela)
print(teste)
"""

galera = list()
dado = list()
totmai = totmen = 0

for p in range(0, 3):
    dado.append(str(input('Digite o nome da pessoa: ')).title())
    dado.append(int(input('Digite a idade da pessoa: ')))
    galera.append(dado[:])
    dado.clear()
print(galera)

for p in galera:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    if p[1] < 18:
        print(f'{p[0]} é menor de idade.')
        totmen += 1
print(f'O total de maiores de idade é {totmai}')
print(f'O total de maiores de idade é {totmen}')


sorted(nums, key=nums.get(1))  # deixax em ordem as keys do dicionario

ranking = sorted(nums.items(), key=itemgetter(1), reverse=True)  # deixa em ordem as keys. precisa importar operator
# O 1 em itemgetter(1) siginifica que irá ordenar a partir dos
# valores, não das keys.
