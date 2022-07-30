# Disparando requests para sites.

import urllib.request

try:
    page = urllib.request.urlopen("http://www.google.com")
except:
    print('\033[31mNão foi possível acessar o Site\033[m')
else:
    print('\033[32mÉ possível acessar o site com sucesso!\033[m')
    page.read()
