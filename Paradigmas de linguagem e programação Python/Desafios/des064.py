#Desafio 064: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
#No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

print()
print('-=-'*8)
print('Soma de Números')
print('-=-'*8)
n = int(input('Entre com um numero [999 para sair]: '))
cont = 0
soma = 0
while n != 999:
    soma += n
    cont += 1
    n = int(input('Entre com um numero [999 para sair]: '))
   
print('Voce digitou {} números e a soma entre eles foi {}.'.format(cont, soma))
print('\nFim...\n')

