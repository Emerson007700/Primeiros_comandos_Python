# (if - significa (se) em bloco e vai ser o bloco verdadeiro (True))
# (else - significa (se não) e vai ser o bloco falso (False)
# Esses são os primeiros comandos condicionais.
# Exempos
tempo = int(input('Quanto tempo tem seu carro: '))
if tempo <= 3:
    print('Por seu carro ter {} anos ele atende os requsitos necessarios'.format(tempo))
else:
    print('Por seu carro ter mais de {} anos ele nao atende o requisito.'.format(tempo))
print('Fim')

# Ou simplificando veja o exemplo
carro = int(input('Quantos anos tem seu carro: '))
print('carro novo'if carro <= 3 else 'Carro velho')

nome = str(input('Qual seu nome: '))
if nome == "Emerson":
    print('Paraben voce foi selecionado.')
else:
    print('Não foi dessa vez.')
print('Bom dia')

n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
m = (n1+n2)/2
print('Sua média foi {}'.format(m))
if m >= 6.0:
    print("Parabens você foi aprovado.")
else:
    print('Voce reprovou.')

