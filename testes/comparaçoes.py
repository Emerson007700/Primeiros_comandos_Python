# Esta usando o ( c que é o primeiro numero a ser lido dentro do laço
# e o 1 é para dar valor a comparação pois ele vai ser o menor e o maior
# pois ainda não sabe que numero vai ser digitada
maior = 0 # Ja vai receber o primeiro valor (1 que esta no primiro (if) para fazer a
          # comparação depois vai receber o numero do segundo (if que esta dentro do else digitado pelo usuario
menor = 0 # Ja vai receber o primeiro valor (1 que esta no primiro (if) para fazer a
          # comparação depois vai receber o numero do segundo no segundo (if que esta dentro do else digitado pelo usuario
for c in range(1, 6):
    numero = int(input('Digite o {} numero: '.format(c)))
    if c == 1:
        maior = numero
        menor = numero
    else:
        if numero > maior: # vai fazer a comparaçao com o (c == 1) pois é o numero para comparação
            maior = numero
        if numero < menor:
            menor = numero
print('O Maior numero é {}'.format(maior))



