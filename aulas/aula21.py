# Funções Parte 2

# Escopo de Variáveis

def teste(b):
    global a   # Faz com que o python use a varável A global
    a = 8  # Sem o global, este A é uma variável local diferente
    b += 5
    c = 2
    print(f'B dentro vale {b}')
    print(f'C dentro Vale {c}')
    print(f'A dentro vale {a}')


a = 4
teste(a)
print(f'A fora vale {a}')


def soma(a=9, b=0, c=0):
    s = a+b+c
    return s  # Return retorna o resultado crú, sem formatação


r1 = soma(2, 3, 7)
r2 = soma(43, 82)
r3 = soma(12, 77, 32)
print(f'A soma dos números {r1} {r2} e {r3} deu {r1+r2+r3}')


def mult(a=1, b=1):
    """
    returns the multiplication between two parameters

    :param a: 1st number of the multiplication
    :param b: 2nd number of the multiplication
    :return: yes
    """
    m = a * b
    return m


print(mult.__doc__)


def fatorial(num=1):
    f = 1
    for i in range(num, 0, -1):
        f *= i
    return f


n = 5
print(f'O fatorial de n é {fatorial(n)}')


def par(num=0):
    if num % 2 == 0:
        return True
    else:
        return False


print(f'\n{par()}')