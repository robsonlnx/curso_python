#  Operadores in e not in
#  Strings são iteráveis
#  0 1 2 3 4 5
#  r o b s o n
# -6-5-4-3-2-1
nome = 'Robson'
print(nome[2])
print(nome[5])
print(nome[-4])
print(nome[-2])

print('==' *10)

print('o' in nome)
print('j' in nome)
print('on' in nome)

print('==' * 10)

print('o' not in nome)
print('onb' not in nome)
print('js' not in nome)

print('==' * 10)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja econtrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')
    