numeros = set([1,2,3,2,4,1,2,7,10,15,20])
print(numeros)

letras = set('abacaxi')
print(letras)

carros = set(('gol', 'gol', 'palio', 'onix', 'onix'))
print(carros)

linguagens = {'python', 'python', 'java'}
print(linguagens)

n1 = {1,2,3,2}
n1 = list(n1)
print(n1[2])

numeros = set([1,2,3,2,4,1,2,7,10,15,20])
numeros = list(numeros)
print(numeros[4])

conj_a = {1,2}
conj_b = {3,4}
conj_a = conj_a.union(conj_b)
print(conj_a)

conj_a = {1,2,3}
conj_b = {2,3,4}
conj_a = conj_a.intersection(conj_b)
print(conj_a)

conj_a = {1,2,3}
conj_b = {2,3,4}
conj_b = conj_b.difference(conj_a)
print(conj_b)

conj_a = {1,2,3}
conj_b = {2,3,4}
conj_b = conj_b.symmetric_difference(conj_a) # retorna o diferente de cada conj.
print(conj_b)

conj_a = {1,2,3}
conj_b = {2,3,4,5,6,1}
conj_b = conj_b.issubset(conj_a) # OS ELEMENTOS DE B NAO ESTAO EM A
print(conj_b)

conj_a = {1,2,3}
conj_b = {2,3,4,5,6,1}
conj_a = conj_a.issubset(conj_b) # todos os elemtos de A estao em B
print(conj_a)

conj_a = {1,2,3}
conj_b = {4,5,6}
conj_a = conj_a.isdisjoint(conj_b) # Nos fala se os conjuntos se repetem em amobos ou não
print(conj_a)

sorteio = {1,2,3}
sorteio.add(42) # adiciona um elemento na lista
print(sorteio)

sorteio = {1,2,3}
sorteio.clear() # Limpa (todo o set)
print(sorteio)

sorteio = {1,2,3}
sorteio.copy() # Faz uma copia
print(sorteio)

sorteio = {1,2,3,10,20,30,10,40,5,42,43}
sorteio.discard(43) # exclui um elemento que foi fornecido,
print(sorteio)

sorteio = {1,2,3,1,2,3,10,20,30,10,40,5,42,43}
sorteio.remove(42) # exclui tb mas se vc pedir para remover um elemento que nao exixte ele vai retornar erro
print(sorteio)

sorteio = {1,2,3,4,5,6,6}
print(len(sorteio)) # Retorna quantos elementos dentro da lista mas nao conta os repetidos

sorteio = {1,2,3,4,5,6,6}
print(1 in sorteio) # retorna verdadeiro ou falso se um elemento esta presente ou nao
print(7 in sorteio)
print(6 in sorteio)



