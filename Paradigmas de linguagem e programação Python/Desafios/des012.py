#Desafio 12 - Escreva um programa que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
print()
print('='*30)
print('Desconto de produto.')
print('='*30)
print()
prod = input('Entre com o nome do Produto para aplicar o desconto: ')
valor = float(input('Qual o preço deste Produto? R$ '))
valor_atual = valor - valor * (5/100)
print('O(A) {} custa R$ {:.2f}!'.format(prod, valor))
print()
print('Agora esse produto {} com 5% de desconto passa a custar: R$ {:.2f}!'.format(prod, valor_atual))
print()

