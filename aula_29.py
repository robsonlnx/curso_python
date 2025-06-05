"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""

numero_str = input('Vou dobrar o número que vc digitar: ')

try:
    numero_float = float(numero_str)
    print('STR:', numero_str)
    print('FLOAT:', numero_float)
    print(f'o dobro de {numero_str} é {numero_float * 2:.2f} ')
except:
    print('Isso não é um número')


