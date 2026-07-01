# desafio 6 - Crie um algoritmo que leia um numero e mostre o seu dobro, triplo e raiz quadrada

print()
n = int (input('Digite um numero: '))
n2 = n * 2
n3 = n * 3
raiz = n**(1/2)
print('\nO numero {} digitado, possui:\n\n{} como seu dobro;\n{} seu triplo;\ne {:.3f} a raiz quadradar!'.format(n, n2, n3, raiz))
print()