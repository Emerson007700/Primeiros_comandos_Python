num = [2, 5, 9, 1]
print(num)
num[2] = 3 # Por se tratar de uma lista posso alterar o elemento dessa formar na o seja o (2 passou a ser 5)
print(num)
num.append(7) # assim é para adicionar um novo elemto
print(num)
num.sort() # vai colocar em ordem
print(num)
num.sort(reverse=True) # vai colocar em ordem decrecente
num.insert(2, 0) # vai inserir o (0) no indice [2] é para definir emque indice quer inserir o elemento
print(num)
num.pop() # vai remover u utimo elemento
print(num)
num.pop(2) # vai remover o indice atribuido
print(num)
num.insert(2,2) # adicionei o 2 no indice 2
print(num)
num.remove(2) # Vai procura do inicio da lista e so vai eliminar o primeiro (2)
print(num)
if 4 in num: # Caso digite para remover um numero que não exita tem que fazer dessa forma no car o 4 não existia
    num.remove(4)
else:
    print('Não achei o numero 4')

numeros = []
for cont in range(0,5): # Comesei com alista vasia (numeros) e o usuario que vai formar essa lista
    numeros.append(int(input('Digite um numero: ')))

valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for c, v in enumerate(valores): # NESSE CASO O ( C ) É O INDICI E O (V) O CONTADOR PARA MOSTRAR A LISTA E FOI USADO O (ENUMEREATE PARA VER ESSA POISIÇAO DA DOS VALORES
    print(f'Na posição {c} encontei {v}!')
print ('FIM')

a = [2, 3, 4, 7]
b = a # AQUI A LISTA (B) TEM UMA LIGAÇAO COM A LISTA (A) ENTAO QUANDO EU INSERIR O (8) NA LISTA (B) O (A) TB VAI MUDAR
b[2] = 8
print(f'Lista A {a}')
print(f'Lista B {b}')

a = [2, 3, 4, 7]
b = a[:] # AGORA A LISTA (B) PEGOU TODOS OS ELEMTOS DE (A) E QUANDO ALTER (B) SOMENTE ELA VAI SE ALTERAR
b[2] = 8
print(f'Lista A {a}')
print(f'Lista B {b}')