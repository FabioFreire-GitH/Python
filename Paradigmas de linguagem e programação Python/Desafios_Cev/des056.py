# Desafio 56: Escreva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa mostre: A media de idade do grupo, o nome do homem mais velho, e quantas mulheres tem menos de 21 anos
print()
print('-=-'*22)
print('Calcula Média Idade, Homem mais Velho e Quantas mulhes menor de 21')
print('-=-'*22)
print()
somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for c in range (1,5):
    print('----- {}ª PESSOA -----'.format(c))
    nome = str(input('Nome: ')).strip().upper()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo (M ou F): ')).strip().upper()
    somaidade += idade
    if c == 1 and sexo == 'M': #ou sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 21:
        totmulher20 += 1

mediaidade = somaidade/4
print('\nA média da idade do grupo é {} anos.'.format(mediaidade))
print('O homem mais Velho tem {} anos e se chama {}.'.format(maioridadehomem, nomevelho))
print('Existe(m) {} mulher(es) menor(es) de 21 anos.'.format(totmulher20))
print('\nFim de programa...\n')

    