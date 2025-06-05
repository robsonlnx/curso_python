"""
Fatiamento de strings
 012345678
 olá mundo
-987654321
Fatiamento [i:f:p] [::]
obs.: a função len retorna a qtd de caracteres da str
"""

variavel = 'Olá Mundo'
print(variavel[5])
print(variavel[-4])
print(variavel[4:])
print(variavel[4:8])
print(variavel[0:5]) # pode omitir o inicio
print(variavel[-8])
print(variavel[-8:-4])
print(len(variavel[3]))
print(len(variavel))
print(variavel[0:len(variavel):1])
print(variavel[0:9:2])
print(variavel[::-1]) # binverte a string
print(variavel[-1:-10:-1])
