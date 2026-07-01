#Desafio 096: Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
def area(l,c):
    a = l * c
    print(f'\nA área do terreno ({l:.2f}x{c:.2f}) é de {a:.2f}m².')


print('-'*30)
print('{:^30}'.format('CONTROLE DE TERRENOS'))
print('-'*30)
larg = float(input('Largura do Terreno (m): '))
comp = float(input('Comprimento do Terreno (m): '))
area(larg, comp)
print()
