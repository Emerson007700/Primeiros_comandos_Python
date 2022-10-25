nome=str(input('Qual seu nome? '))
if nome == 'Emerson':
    print('Você será um exelente programador python')
else:
    print('Sinto muito mas você não receberá o premio')
print('Bom dia {}!'.format(nome))

n1=float(input('Qual a nota da sua prova? '))
n2=float(input('Qual a nota da sua segunda prova?'))
m=(n1+n2)/2
print('Sua média é {}.'.format(m))
if m>=6.0:
    print('(Aprovado) \nVoçê esta na média, parabens.')
else:
    print('(Reprovado) \nVoçê esta abaixo da média permitida, por vafor estude mais.')