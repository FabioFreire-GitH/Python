#Desafio  066: Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
# No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).
print()
print('-=-'*8)
print('Soma de Números 2.0')
print('-=-'*8)
n = soma  = cont = 0
while n != 999:
    n = int(input('Digite um número [999 para sair]: '))
    if n == 999:
        break
    soma += n
    cont += 1
print(f'\nVocê digitou {cont} números e a soma entre eles é {soma}.')
print('\nFim...\n')

