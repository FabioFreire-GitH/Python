#Desafio 30 - Escreva um programa que leia um numero inteiro e mostre na tela se ele é PAR ou Impar.
print()
print('='*30)
print('Par ou Impar')
print('='*30)
print()
n = int(input('Digite um numero: '))
if n % 2 == 0:
    print('{} é um número PAR!'.format(n))
else:
    print('{} é um número IMPAR!'.format(n))
print('FIM...')
print()
