# Notas da turma

def notas(*n, sit=False):
    s = dict()
    lista = list()
    for i in n:
        lista.append(i)
    s['Total'] = len(lista)
    s['Maior'] = max(lista)
    s['Menor'] = min(lista)
    s['Media'] = float(f"{sum(lista) / s['Total']:.2f}")
    if sit is True:
        if s['Media'] >= 7:
            s['SITUAÇÃO'] = 'BOA'
        elif 7 > s['Media'] >= 5:
            s['SITUAÇÃO'] = 'ABAIXO DO ESPERADO'
        elif s['Media'] < 5:
            s['SITUAÇÃO'] = 'TERRÍVEL'
    lista.clear()
    return s


resul = notas(3.9, 9, 7.4, 10, 7, sit=True)
for k, v in resul.items():
    print(k, v)


