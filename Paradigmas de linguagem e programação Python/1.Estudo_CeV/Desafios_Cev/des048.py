# Desafio 48: Escreva um programa que calucule a soma entre todos os numeros impares que são multiplos de tres e que se encontram no intervalo de 1 ate 500

print()
print('-=-'*8)
print('Soma Números Impares')
print('-=-'*8)
print()
soma = 0
for c in range(1,500): 
    if c % 3 == 0:
        soma += c
print (soma)
print('\nFim...\n')