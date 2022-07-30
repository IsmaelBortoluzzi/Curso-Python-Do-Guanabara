#Condições aninhadas

p = str(input('Qual o país mais grande?')).capitalize()

if p == 'Rússia':
    print('\033[32m Certa resposta! hahá \033[m')

elif p == 'Canadá':
    print('\033[33m Passou perto \033[m')

elif p == 'Alemanha':
    print('A Alemanha é o melhor país, mas não é o mais grande')

else:
    print('\033[31m ERRRROOOUU \033[m')
    print('Precisa estudar mais geografia.')

