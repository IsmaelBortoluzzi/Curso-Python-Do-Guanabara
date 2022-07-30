# Tratamento de erros e exceções

"""
try:
    a = int(input('Digite o numero 1: '))
    b = int(input('Digite o numero 2: '))
    r = a / b
except:
    print(f"Um problema foi encontrado.")
else:
    print(f'O resultado foi {r}')
finally:
    print('Volte sempre!')
"""
"-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-="

try:
    a = int(input('Digite o numero 1: '))
    b = int(input('Digite o numero 2: '))
    r = a / b
except Exception as erro:
    print(f'O problema encontrado foi {erro.__class__}')
else:
    print(f'O resultado foi {r}')
finally:
    print('Volte sempre!')

"-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-="
"""
try:
    a = int(input('Digite o numero 1: '))
    b = int(input('Digite o numero 2: '))
    r = a / b
except (ValueError, TypeError):
    print(f'Você digitou um valor inválido!')
except ZeroDivisionError:
    print(f'Não existe divisão por 0')
except KeyboardInterrupt:
    print(f'Você não finalizou a digitação!')
else:
    print(f'O resultado foi {r:.2f}')
finally:
    print('Volte sempre!')
"""