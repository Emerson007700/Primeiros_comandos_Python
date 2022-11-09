soma = 0
for c in range(0 , 3): # UNCA ESQUEÇA DOS ( : ) NO FINAL
    n1 = int(input('Digite um valor: ')) # vai repetir o comando de acordo com o valor atribuido
    soma = soma + n1 # pode ser tb assim: (soma+= n1) vai dar o mesmo resultado
print('Fim {}'.format(soma))
