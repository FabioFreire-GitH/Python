#Desafio 33 - Escreva um programa que leia tres numeros e mostre qual é o maior e qual é o menor.
print()
print('='*30)
print('Qual é o Maior e o Menor Valor')
print('='*30)
print()

n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
n3 = int(input('Digite o terceiro numero: '))
#Verifica quem é menor
menor = n1
if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3

# Vefirica quem é o maior
maior = n1
if n2>n1 and n2>n3:
    maior = n2
if n3>n1 and n3>n2:
    maior = n3

print('\nO maior número é: {}'.format(maior))
print('\nO menor número é: {}'.format(menor))
print()


