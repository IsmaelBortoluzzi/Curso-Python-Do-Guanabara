# Input com erro do int concertado:

def leiaint(i=''):
    while True:
        h = input(i)
        if h.isnumeric():
            h = int(h)
            return h
        else:
            print('\033[31mERRO. Digite um número inteiro!\033[m')


a = leiaint('Digite um número inteiro: ')
print(a)
