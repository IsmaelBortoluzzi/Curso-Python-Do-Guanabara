# Aprimorando Dicionários

jogador = dict()
jogadores = list()
partidas = list()

while True:
    print('-=' * 25)
    jogador['Nome'] = str(input('Digite o nome do jogador: '))
    tot = int(input(f'Quantas partidas o jogador {jogador["Nome"]} jogou? '))
    for c in range(0, tot):
        partidas.append(int(input(f'    Quantos gols na partida {c+1} ')))
    jogador['Gols'] = partidas[:]
    jogador['Total'] = sum(partidas)
    jogadores.append(jogador.copy())
    jogador.clear()
    partidas.clear()
    q = str(input('Quer continuar?')).strip().upper()
    if q == "N":
        break
print('-='*65)

print('cod   ', end='')
for i in jogadores[0].keys():
    print(f'{i:<24}', end='')
print('')

print('-'*65)
for k, v in enumerate(jogadores):
    print(f'{k:>4}  ', end='')
    for d in v.values():
        print(f'{str(d):<20}', end='')
    print('')
print('-'*25)

print('-='*25)

while True:
    d = int(input('Queres os dados de aproveitamento de qual jogador?'))
    for i in range(len(jogadores[d]['Gols'])):
        print(f'Na partida {i+1} ele fez {jogadores[d]["Gols"][i]} gols.')
    q = str(input('Quer continuar?')).strip().upper()
    if q == "N":
        break
