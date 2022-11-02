# laco de repetiçao ou iteração
for c in range(1,10): # ESSA LINHA É O PASSO E DENTRO DO () SE ATRIBUI O QUE QUER Q FAÇA
    print('Oi')
print('fim')

for c in range(0, 6):
    print(c) # fez a contagem só q não incluiu o 6 pois ele contas o elemnto pode
             # acrencentar +1 ou so colocar 7 em vez de 6
print('fim')

for c in range(0, 7, 2): # Vai contar de 2 em 2 ou o que for atribuido no final
    print(c)
print('fim')

for c in range(6, 0, -1): # Aqui ele vai fazer a contagem de traz pra frente mas tem que colocar o (-1)
    print(c) # O ( c ) é o contador

n = int(input("Digite um numero: "))
for c in range(0, n+1): # O ( n ) é a valor atribuido pelo usuario
    print(c) # O (c) é o contador pode ser qualquer letra ou nome.
print('Fim')

i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p): # ESSA LINHA É O PASSO E DENTRO DO () SE ATRIBUI O QUE QUER Q FAÇA (PODE ATRIBUIR O VAR DO USUARIO
    print(c)
print('Fim')

