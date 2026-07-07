#Desafio 15 - Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. 
#Calcule o preço a pagar, sabendo que o carro custa R$60 por dias e R$ 0,15 por KM rodado.
print()
print('='*30)
print('Locadora de Veiculos')
print('Calculo diaria')
print('='*30)
print()
diaria = 60.00
km = 0.15
print('Sistema de Devolução de Carro')
dias = int(input('\nDigite aqui a quantidade de dias locados: '))
km_rodado = float(input('\nDigite aqui a quantidade de KM rodado: '))
valor = (diaria * dias) + (km_rodado * km)
print('\nO valor do aluguel do carro é R$ {:.2f}'.format(valor))
print()

