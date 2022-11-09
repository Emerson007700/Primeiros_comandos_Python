# (while not) # Enquanto não (Se usa quando vc não sabe ate quando vai ser presizo repetir
c = 1 # adicionamos o contator
while c <= 10: # enquanto c <= 10 ele vai contar, se não tivesse aquele igual ia so ate 9
    print(c, end=" - ")
    c = c + 1
print("Fim")

'''n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print('Fim')'''

'''r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer contunuar? ')).upper()
print('fim')'''

n = 1
par = 0
impar = 0  # Pode ser feito assim tb (par = impar = 0)
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0: # foi colocado isse if para quando o usuario digitar o (0) encerrar e nao contar junto como um numero
        if n % 2 == 0:
            par = par + 1
        else:
            impar = impar + 1
print('{} numeros pares e {} numeros impares'.format(par, impar))