# TUPLAS SÃO IMUTAVEIS
lanche = ('Hamburgue', 'suco', 'pizza', 'pudim')
print(len(lanche)) # Leu quantos elementos tem na tupla
print(sorted(lanche))
print(lanche)
print(lanche[0])
print(lanche[1])
print(lanche[2])
print(lanche[3])
print(lanche[-2]) # vai ler de traz para frante
print(lanche[1:3]) # Fatiamento de indice 1 ate o 3 lembrando que ele vai iguinorar o 3
print(lanche[:2]) # vai ler do inico ate o elemento o indicie 1 vai ignoraro o 2
print(lanche[2:]) # vai ler do indice 2 ate o final
for comida in lanche:
    print(f'Vou comer {comida}')
print('Estou satisfeito')

for cont in range(0, len(lanche)):# esse maneira e vai apresentar o mesmo resultado
    print(f'{lanche[cont]} na posição {cont}')
for pos, comida in enumerate(lanche):
    print(f'Evou comer {comida} na posição {pos}') # vai mostrar a posição

a = 1, 2, 3, 4
b = 10, 20, 15, 50, 4, 3
c = b + a # vai aparecer na posição da cada entao se a + b vai aparecer diferente
print(c)
#print(c.count(4).index(15)) # vai mostrar quantas vezes aparerecu o numero 4
print(c.index(15)) # vai mostrar em que posição ele esta
