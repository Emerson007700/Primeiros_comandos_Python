# stylo 0, 1, 4, 7
# Texto                   Background
# 30 - (branco),           40
# 31 - (vermelho),         41
# 32 - (verde),            42
# 33 - (amarelo),          43
# 34 - (azul),             44
# 35 - (violeta),          45
# 36 - (azul ciano),       46
# 37 - (cinza}             47
#\033[0;30;41m
print('\033[4;31;44mOla Mundo!\033[m')
print('\033[4;34mOla Mundo!\033[m')
n1=int(input("Digite um valor= "))
n2=int(input("Digite outro numero= "))
s= n1+n2

print('A soma entre \033[1;32m{} e \033[1;34m{} é \033[1;33m{}'.format(n1, n2, s))