#Desafio 16 - Escreva um programa que leia um numero Real qualquer pelo teclado e mostre na tela a sua porção inteira. EX 6.127 - inteiro 6.
print()
print('='*30)
print('Mostra porção inteira')
print('='*30)
print()
from math import trunc
num = float(input('Digite um valor Real: '))
print('\nA parte inteira é: {}'.format(trunc(num)))
print()

# Dá para fazer sem importar a biblioteca math -> .format(int(num))