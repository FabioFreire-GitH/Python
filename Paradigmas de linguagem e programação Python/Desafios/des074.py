#Desafio 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
from random import randint
numeros = (randint(1,9),randint(1,9),randint(1,9),randint(1,9),randint(1,9))
maior = max(numeros)
menor = min(numeros)
print(f'\nNúmeros Sorteados: {numeros}')
print(f'\nO Número Maior é: {maior}')
print(f'\nO Número Menor é: {menor}')
print()

