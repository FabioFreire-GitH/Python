# Desafio 54: Escreva um programa que leia o ano de nascimento de sete pessoas. No final mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
print()
print('-=-'*8)
print('Verifica Maior idade')
print('-=-'*8)
print()
menor = 0
maior = 0
for c in range (1, 8):
    ano = int(input('Em que ano a {}ª pessoa nasceu: '. format(c)))
    if len(str(ano)) != 4 or ano > date.today().year:
        print ('Ano Invalido!')
        break
    if ano == 0:
        ano = date.today().year
    idade = date.today().year - ano
    if idade < 18:
        menor += 1
    else:
        maior += 1
print('\n{} pessoas são menores e {} pessoas são maiores de idade.'.format(menor, maior))
print('\nFim...\n')
