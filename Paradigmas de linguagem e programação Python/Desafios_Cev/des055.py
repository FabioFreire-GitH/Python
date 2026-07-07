# Desafio 55: Escreva um programa que leia o peso de cinco pessoas. Nofinal, mostre qual foi o maior e o menor peso lidos.
print()
print('-=-'*8)
print('Verifica Maior e Menor Peso')
print('-=-'*8)
print()
maior = 0
menor = 0
for c in range (1, 6):
    peso = float(input('Entre com o peso da {}ª pessoa: '.format(c)))
    if maior == 0 and menor == 0:
        menor = peso
        maior = peso
    elif peso <= menor:
        menor = peso
    elif peso >= maior:
        maior = peso
print ('\nMaior peso {:.2f}Kg | Menor peso {:.2f}Kg\n '.format(maior, menor))
print('Fim de programa...\n')



