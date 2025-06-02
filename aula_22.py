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

if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')
print('==' * 10)

print(True or True)
print(True or False)
print(False or True)
print(False or False)

print(0 or False or 0 or 'abc' or True)
