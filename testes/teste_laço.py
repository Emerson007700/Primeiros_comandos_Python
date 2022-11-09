# Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho
# e quantas mulheres têm menos de 20 anos.
soma = 0
tot = 0
maior = 0
maisvelho = ''
for c in range(1, 5):
        nome = str(input('Qual o nome da {}º pessoa? '.format(c)))
        idade = int(input('Qual a idade? '))
        sexo = str(input('Qual o sexo (M) OU (F)? ')).upper()
        print('-=-' * 12)
        soma = soma + idade
        if c == 1 and sexo == "M":
                maior = idade
                maisvelho = nome
        elif idade > maior and sexo == "M":
                maior = idade
                maisvelho = nome
        else:
                if sexo == "F" and idade < 20:
                        tot = tot +1

print('O mais velho é {} e sua idade é {} e tem {} mulhes abaixo de 20 anos a media da idade é {}'.format(maisvelho, maior,tot, soma/c))

