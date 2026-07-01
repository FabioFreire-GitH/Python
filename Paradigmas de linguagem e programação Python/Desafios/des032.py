#Desafio 32 - Escreva um programa que leia um ano qualquer e mostre se ele é BISSEXTO.
print()
print('='*30)
print('Ano BISSEXTO')
print('='*30)
print()
ano = int(input('Digite um Ano com quatro posições: '))
if ano % 4 == 0: # melhor formula : if ano % 4 == 0 and ano %100 != 0 or ano % 400 == 00:
    if ano % 100 == 0:
        if ano % 400 == 0:
            print('É Bissexto!')
        else:
            print('Não é Bissexto!')
    else:
        print('É Bissexto!')
else:
    print('Não é Bissexto!')
print('FIM...\n')

'''
import datetime ou from datetime impor date

if ano == 0:
    ano = date.today().year #usando o from, pega na date do hoje só o ano.

'''