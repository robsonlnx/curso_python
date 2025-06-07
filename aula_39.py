"""
Iterando strings com while
"""

# nome = 'Robson Oliveira'  # strings são iteráveis
nome = input('Digite seu nome: ')

indice = 0
novo_nome = ''

while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1

novo_nome += '*'
print(novo_nome)

    