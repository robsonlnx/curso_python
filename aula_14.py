a = 'A'
b = 'B'
c = 1.1

string = 'a={} b={} c={:.2f}'
formato_1 = string.format(a, b, c)
print(formato_1)

# por posição
string = 'a={0} b={1} c={2:.2f}'
formato_2 = string.format(a, b, c)
print(formato_2)

# parametro nomeado
string = 'a={nome1} b={nome2} c={nome3:.2f}'
formato_3 = string.format(nome1=a, nome2=b, nome3=c)
print(formato_3)

