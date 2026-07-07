#Desafio 46: Escreva um programa que mostrea a contagem regressiva para o estouro de fogos de artificio. (indo de 10 até 0 com uma pausa de 1 segundo entre eles)
from time import sleep
print()
print('-=-'*8)
print('Contagem Regrassiva')
print('-=-'*8)
print()
for c in range (10, -1, -1):
    print(c)
    sleep(1)
print('\nFim\n')

