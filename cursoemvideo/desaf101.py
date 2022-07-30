# Voto

def voto(v):
    from datetime import date
    """
    :param v: Type year of birth
    :return: yes
    """
    idade = date.today().year - v
    if idade < 16:
        return f'Com {idade} anos o voto é NEGADO.'
    elif 18 > idade >= 16 or idade >= 65:
        return f'Com {idade} anos o voto é OPCIONAL.'
    else:
        return f'Com {idade} anos o voto é OBRIGATÓRIO.'


j = int(input('Ano de nascimento: '))
print(voto(j))