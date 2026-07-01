#Desafio 28: O computador escolhe um numero de 0 a 5 e o usuario tenta advinhar o numero gerado. O programa deverá esvrever na tela se o usuario venceu ou perdeu.
print()
print('='*30)
print('Advinhe o Número')
print('='*30)
print()
import random # ou from random import randint
c = random.randint(0, 5)
j = int(input('Digite um numero de 0 a 5: '))

if j < 0 or j > 5:
    print('\nNúmero invalido!')
elif j == c:
    print('\nNúmeros Iguais!!! Você VENCEU!!!')
    print ('O computador escolheu {} e o usuário {}!'.format(c, j))
else:
    print('\nNúmeros Diferentes!!! Você PERDEU!!!')
    print ('O computador escolheu {} e o usuário {}!'.format(c, j))
print('\nFim do Programa...')
print()

# import time ou 
# form time import sleep (o computador espera alguns segundos)
# sleep (2) - coloca os segundos de espera