# Operadores lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser verdadeiras.
# Se qualquer valor for considerado falso,
# a expressão inteira será avaliada naquele valor
# São considerados false (já vimos antes)
# 0 0.0 '' False
# Também existe  tipo None que é usado para 
# representar um não Valor 
entrada = input('[E]ntrar ou [S]air: ')
senha_digitada = input('Senha: ')
senha_permitida = '123456'

if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')
print('==' * 10)
print(True and True)
print(True and False)
print(False and True)
print(False and False)
print('')

