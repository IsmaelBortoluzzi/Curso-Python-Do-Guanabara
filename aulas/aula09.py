# Manipulação de string

frase = ('curso em vídeo python')

# Fatiamento

print(frase[0:5])
print(frase[0:8:2])
print(frase[:3])
print(frase[4::2])

# Análise

print(len(frase))
print(frase.count('o'))
print((frase.count('o', 0, 13)))
print(frase.find('ví'))
print('vídeo' in frase)

# Transformação

#frase = ('curso em vídeo python')

print(frase)
print(frase.replace('em vídeo python', 'chupando buceta direito'))
print(frase.upper())
print(frase.capitalize()) #manda a 1° letra pra maiuscula
print(frase.title()) #manda a 1° letra de toda palavra da str pra maiuscula

'''frase.strip()''' #Enlimina os espaços inúteis antes e depois da string
'''frase.rstrip()''' #Enlimina espaços inúteis à direita da string
'''frase.lstrip()''' #Enlimina espaços inúteis à esquerda da string

# Divisão

print(frase.split())
print('~'.join(frase))

# Uso de aspas duplas 3 vezes

print("""Germans (German: Deutsche) are a Germanic ethnic 
group native to Central Europe, who share a
common German ancestry, culture, and history. 
German is the shared mother tongue
of a substantial majority of ethnic Germans.
The English term Germans has been the name
for the German-speaking population of the Holy
Roman Empire since the Late Middle Ages.
Ever since the onset of the Protestant Reformation
within the Holy Roman Empire in the 16th century,
German society has been characterized by a Catholic-Protestant
divide.""")