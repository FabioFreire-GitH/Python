#Desafio 31 - Escreva um programa que leia a distancia de uma viagem em Km. Calcule o preço da passagem, cobando R$0,50 por km para viagens de até 200km e R$ 0,45 para viagens mais longas.
print()
print('='*30)
print('Distancia de Viagem')
print('='*30)
print()
d = int(input('Digite a distancia da Viagem: '))
if d <= 200:
    p = float(d * 0.50)
else:
    p = float(d * 0.45)
print('A distancia da viagem é {} Km e custará R$ {:.2f}.'.format(d,p))
print('FIM...\n')
