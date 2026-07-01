#Desafio 10 - Escreva um programa que leia quanto uma pessoa tem na carteira e mostre quantos dolares ela pode comprar
print()
print('='*30)
print('Conversão de Moedas')
print('='*30)
print()
real = float(input('Quanto dinheiro você tem na carteira? R$ '))
cotacao = float(input('Qual a cotação atual do Dolar? R$ '))
dolar = real/cotacao
print('\nNa atual cotação (R$ {:.2f}), você pode comprar US${:.2f} Dólares!'.format(cotacao, dolar))
print()

