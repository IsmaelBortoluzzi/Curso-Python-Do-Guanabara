# Ficha do jogador

def ficha(nome='<desconhecido>', gols='0'):
    if nome == '' and gols == '':
        return f'O jogador <desconhecido> fez 0 gols.'
    if nome == '':
        return f'O jogador <desconhecido> fez {gols} gols.'
    if gols == '':
        return f'O jogador {nome} fez 0 gols.'

    return f'O jogador {nome} fez {gols} gols no campeonato.'


while True:
    jog = str(input('Jogador: '))
    gol = str(input('Gols: '))
    print(ficha(jog, gol))
    if jog == '999' or gol == '999':
        break
