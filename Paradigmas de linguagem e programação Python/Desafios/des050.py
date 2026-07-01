# Desafio 50: Escreva um programa que leia seis numeros inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for impar, desconsidere-o.
print()
print('-=-'*8)
print('Mostra os Valores Pares')
print('-=-'*8)
print()
n = ['','','','','','']
soma = 0
for c in range(0,6):
    n[c] = int(input('Digite um número: '))
    if n[c] % 2 == 0:
        soma += n[c]
print('\n A soma dos numeros pares é: {}.'.format(soma))
print()
###################################
# SOLUCAO GUANABARA ABAIXO - MELHOR
###################################
print('-=-'*8)
print('Soluçao Guanabara')
print('-=-'*8)
print('Mostra os Valores Pares')
print('-=-'*8)
print()
soma = 0
cont = 0 #(contador para contar os seis numeros do desafio)
for c in range(1,7):
    n = int(input('Digite o {} número: '.format(c)))
    if n % 2 == 0:
        soma += n
        cont += 1
print('\nVocê informou {} números pares e a soma foi: {}.'.format(cont, soma))
print()
