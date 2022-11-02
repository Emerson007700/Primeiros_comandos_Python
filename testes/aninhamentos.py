# if = se
# elif = se nao se
# else = se não

nome = str(input('Qual o seu nome? '))
if nome == 'Emerson':
    print('Voce foi escolhido')
elif nome == 'Pedro' or nome == 'Rodrigo' or nome == 'João': # Aqui ele gera outra condiçao e pode ser aplicado varios (elif)
    print('Seu nome não esta na lista de convidados')      # mas so pode ser aplicado apos o if
elif nome in  'Julia Ana Priscila Maria':
    print("Por se tratar de uma mulher voce esta esta lista.")
else:
    print('Tente outra vez') # A condiçao (else) só pode ser aplica uma unica vez diferentemente do (elif) e não precisa
                             # ter caso não queira ele é opcional.

print('Tenha um bom dia {}'.format(nome))