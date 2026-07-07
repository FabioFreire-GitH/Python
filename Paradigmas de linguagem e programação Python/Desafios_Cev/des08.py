#Desafio 8 - Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.
print()
print('='*50)
print('Conversão de medidas')
print('Metros para centímentros e milímetros')
print('='*50)
print()
valor = float(input('Informe a medida em Metros: '))
cm = valor * 100
mm = valor * 1000
print('Convertendo...')
print('\nEm centímetros: {:.1f} cm'.format(cm))
print('Em milímetros: {:.1f} mm'.format(mm))
print()