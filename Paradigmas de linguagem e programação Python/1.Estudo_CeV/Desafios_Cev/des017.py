#Desafio 17 - Escreva um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa.
print()
print('='*30)
print('Calcula a Hipotenusa')
print('='*30)
print()
from math import hypot
cat_op = float(input('Entre com o cateto oposto: '))
cat_ad = float(input('\nEntre com o cateto adjacente: '))
hipo = hypot(cat_op, cat_ad)
print('\nA hipotenusa é: {:.2f}'.format(hipo))
print()

# ou 
# from math import sqrt
# h = sqrt(cat_op**2 + cat_ad**2)

# ou sem importat
# h = (cat_op ** 2 + cat_ad ** 2) ** (1/2)

