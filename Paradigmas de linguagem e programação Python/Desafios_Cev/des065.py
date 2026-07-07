#Desafio 065: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
#O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

print()
print('-=-'*8)
print('Médio de Números')
print('-=-'*8)
n = cont = soma = media = maior = menor = 0
resp = 'S'
while resp in 'Ss':
    n = int(input('Entre com um numero: '))
    soma += n
    cont += 1
    if cont == 1:
        menor =  maior = n   
    elif n <= menor:
        menor = n
    elif n >= maior:
        maior = n
    resp = str(input('Deseja Continuar? [S/N] ')).strip().upper()[0]
media = soma / cont
print('\nVoce digitou {} números e a media entre eles é {:.2f}.'.format(cont,media))
print('\nMaior {} | Menor {} '.format(maior, menor))
print('\nFim...\n')
