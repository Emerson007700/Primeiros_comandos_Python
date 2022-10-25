nome=input('Qual seu nome: ')
print('Prazer em te conhecer {:^20}!'.format(nome))
print('Prazer em te conhecer {:>20}!'.format(nome))
print('Prazer em te conhecer {:<20}!'.format(nome))
print('Prazer em te conhecer {:=<20}!'.format(nome))
print('Prazer em te conhecer {:=>20}!'.format(nome))
print('Prazer em te conhecer {:=^20}!'.format(nome))

n1=int(input('Digite um valor: '))
n2=int(input('Digite outro valor: '))
s=n1+n2
m=n1*n2
d=n1/n2
di=n1//n2
dr=n1%n2
e=n1**n2
print('A soma vale: {} a multiplicação {} a divisão {:.3f} \n A divisão inteira {} o resto da dvisão {} e o exponente {}'.format(s,m,d,di,dr,e))
