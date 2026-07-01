# Desafio 51: Escreva um programa leia o primeiro termo e a razão de um PA (progressão aritmetica). No final, mostre os 10 primeiros termos dessa progressão.
print()
print('-=-'*8)
print('Progressão Aritmética')
print('-=-'*8)
print()
a1 = int(input('Entre com o primeiro Termo: '))
r = int(input('Entre com a razão: '))
p = int(input('Entre com a Posição desejada: '))
ap = a1 + (p-1)*r
print('PA = (', end =' ')
for c in range (a1, ap+1, r): #O guanabara colocou (a1, ap+r, r)
    print('{}'.format(c), end = ', ')
print(')')
print('\nSaindo do programa...\n')
    
