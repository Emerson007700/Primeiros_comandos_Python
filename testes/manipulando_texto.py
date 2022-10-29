frase = 'Curso em Video Python'
print(frase[3]) # Vai pegar so a letra que na posição informada no caso começa contando do zero vai retornar o (s)
print(frase[3:13]) # Vai monstrar da posição 3 ate a 13 vai retornar (so em Vide) vai contar os espaços tb
print(frase[:13]) # Vai contar do inicio ate a posição 13
print(frase[1:15]) # Vai contar do 1 ate a posição 13
print(frase[1::2]) # Vai começar do 1 vai saltar de 2 em 2
print(frase.count('y')) # esta função vai contar quantas vezes o (y) apareceu ou o Valor atribuido
print(frase.count('o',0,13)) # Vai mostra da posição (0) ate a posição (13) quantos (o) tem
print(len(frase)) # Vai contar quantos caracteres incluindo os espaços
print('-'.join(frase)) # Vai juntar todos os elemtos com ( - ) ou o valor informado
print(frase.replace('Video','Aula')) # Vai procurar (Video) e vai subistituir por (Aula) mas não vai armazenar
print('Curso' in frase) # Está perguntando se Curso existe em frase se existir vai retornar (True) caso não (False)
print(frase.find('Python')) # Vai mostrar em que posição ele encontra a palavra (Python)
print(frase.find('python')) # Se não existir vai retornar (-1)
print(frase.lower().find('python'))
print(frase.split()) # Vai dividar as palavras e contar apartir de casa palavra. Tecnicamente gera uma lista.
print(frase.upper()) # O que não for maiusculo ele vai transformar em mauisculo.
print(frase.lower()) # Vai transformar o que for maiusculo para minusculo.
print(frase.capitalize()) # Vai transformar tudo em minusculo e depois colocar só a primeira letra da frase em maiusculo.
print(frase.title()) # Vai transformar tudo em minusculo e depois colocar a primeira letra de cada palavra em maiusculo.
frase2 = '    Aprenda Python    '
print(frase2.strip()) # Vai remover os espaços tanto no incio das frases quanto no final
print(frase2.rstrip()) # Vai remover somente os espaços do lado direito.
print(frase2.lstrip()) # Vai remover somente os espaços do lado esquerdo.
