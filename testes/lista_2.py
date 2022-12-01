teste = []
teste.append('Gustavo')
teste.append(40)
galera = []
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 25
galera.append(teste[:])
print(galera)

classe = [['João', 45], ['Maria', 40], ['Pedro', 35], ['Marcos', 15]]
print(classe[1][0]) # veja aqui aqui estou pedindo para mostrar o indice 1 na posição 0 dessa lista

for p in classe:
    print(p)
for p in classe:
    print(f'{p[0]} tem {p[1]} anos de idade')

galera2 =[]
dados = []
totmai = totmen = 0
for c in range(0, 3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    galera2.append(dados[:]) #Copiou
    dados.clear()
print(galera2)
for p in galera2:
    if p[1] >= 21:
        print(f'{p[0]} e maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} e menor de idade')
        totmen += 1
print(f'{totmai} Pessoa é maior de idade e {totmen} pessoas é menor de idade')