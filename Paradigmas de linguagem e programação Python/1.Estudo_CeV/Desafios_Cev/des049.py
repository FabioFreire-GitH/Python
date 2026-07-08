# Desafio 49: Escreva um programa pra refazer o desafio 009 mostrando a tabuada que o usuario escolher, so que agora utilizando um laço for.
print()
print('-=-'*4)
print('Tabuada')
print('-=-'*4)
print()
valor = int(input('Digite um número: '))
print()
print('-=-'*4)
for c in range(0, 11):
    print('{} x {:2} = {}'.format(valor, c, valor * c))
print('-=-'*4)
print('\nFim...\n')