# Desafio 42: Escreva um programa Refaça o desafio 35 acrescentado o recurso de mostrar que tipo de triangulo será formado (equilatero todos iguais; isosceles dois iguas ou escalenos todos diferentes)
print()
print('='*30)
print('Analisador de Triângulos 2.0')
print('='*30)
print()
s1 = float(input('Digite o primeiro Segmento de Reta em (cm): '))
s2 = float(input('Digite o segundo Segmento de Reta em (cm): '))
s3 = float(input('Digite o terceiro Segmento de Reta em (cm): '))

if (s1 < s2 + s3) and (s2 < s1 + s3) and (s3 < s1 + s2):
    print('\nOs Segmentos PODEM formar um Triângulo.')
    if s1 == s2 and s2 == s3:
        print('\nTriângulo Equilátero!')
    elif s1 != s2 and s2 != s3:
        print('\nTriângulo Escaleno!')
    else:
        print('\nTriângulo Isosceles!')
else:
    print('Segmentos informados NÃO formam um Triângulo.')
print("\nFIM...\n")
