# cores no terminal

# print('\033[1;34;40m FÜR DEUTSCHLAND \033[m')

# print('\033[7;34;40m FÜR DEUTSCHLAND \033[m')

panzer = 'Tiger 1'
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'vermelho': '\033[31m',
         'preto': '\033[7;40m',
         'branco': '\033[30m',
         'verde': '\033[32m'}

a = 'Deutschland'
print('\033[7;30m O país com 150% de diciplina é: \033[m {}{}{}'
      .format('\033[1;34;40m', a, '\033[m'))

print(cores['azul'], 'Tiger II', cores['limpa'])