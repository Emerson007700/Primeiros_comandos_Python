cont = 0
s = 0
while True:
    n1 = int(input('Digite um numero: '))
    if n1 == 999:
        break # interrompe o laço sai sai
    s += n1
    cont += 1 # o contador vai ficar fora e não vai contar o ultimo comando oi seja o 999
print(f'{cont} a soma é {s} e média é {s/cont}')