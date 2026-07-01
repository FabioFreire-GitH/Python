#Desafio 24 - Escreva um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".
print()
print('='*30)
print('Nome da Cidade')
print('='*30)
print()
cidade = str(input('Em que cidade você nasceu? ')).strip()
print(cidade[:5].upper == 'SANTO')
print()
