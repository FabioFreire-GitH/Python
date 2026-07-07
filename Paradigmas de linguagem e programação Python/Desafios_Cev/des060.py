#Desafio 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.
#Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120
from math import factorial
print()
print('-=-'*20)
print('Cálculo de Fatorial com a Função expecífica de Fatorial')
print('-=-'*20)
n = int(input('Entre um número cara calcular se Fatorial: '))
f = factorial(n)
print ('O fatorial de {} é {}.'.format(n,f))
print()
print('-=-'*20)
print('Cálculo de Fatorial sem Função de Fatorial')
print('-=-'*20)
n = int(input('Entre um número cara calcular se Fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end = ' ')
while c > 0:
    print ('{} '.format(c), end = '')
    print (' X ' if c > 1 else ' = ', end=' ')
    f = f * c #ou f = f * c
    c -= 1
print('{}.'.format(f))

