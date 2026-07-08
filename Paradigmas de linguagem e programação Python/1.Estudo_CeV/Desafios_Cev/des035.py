#Desafio 35 - Escreva um programa que leia o comprimento de tres retas e diga ao usuario se elas podem ou nao formar um triangulo.
print()
print('='*30)
print('Analisador de Triângulos')
print('='*30)
print()
s1 = float(input('Digite o primeiro Segmento de Reta em (cm): '))
s2 = float(input('Digite o segundo Segmento de Reta em (cm): '))
s3 = float(input('Digite o terceiro Segmento de Reta em (cm): '))

if (s1 < s2 + s3) and (s2 < s1 + s3) and (s3 < s1 + s2):
    print('\nOs Segmentos PODEM formar um Triângulo.')
else:
    print('Segmentos informados NÃO formam um Triângulo.')
print("\nFIM...\n")
