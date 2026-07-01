#Desafio 23 - Escreva um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos dogotos separados. Ex.: 1834 / unidade 4 / dezena 3 / centena 8 / milhar 1
print()
print('='*30)
print('Analise um Número')
print('Entre 0 a 9999')
print('='*30)
print()
num = int(input('Entre com um número: '))
print()
#n = str(num) - Dá erro se usar menos de 4 digitos o numero digitado, onde no format usaria .format(n[3]) para unidade e etc ate milhar . format(n[0])  
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('Analisando o número {}'.format(num))
print()
print('Unidade: {}'.format(u)) 
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
print()