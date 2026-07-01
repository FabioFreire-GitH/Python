# Desafio 52: Escreva um programa que leia um numero inteiro e diga se ele é ou não um numero primo.
print()
print('-=-'*6)
print('Número Primo')
print('-=-'*6)
print()
n = int(input('Entre com un número: '))
cont = 0
print()
print('Testando os números divisiveis...')
for c in range(1, n + 1):
    if n % c == 0:
        print('{}'.format(c), end = ' ')
        cont += 1
if cont == 2:
    print('\n\nO número {} é PRIMO!'.format(n))
else:
    print('\n\nO número {} NÃO é PRIMO!'.format(n))
print('\nFim..\n')
