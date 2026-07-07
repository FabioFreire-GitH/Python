#Desafio 27 - Escreva um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente.
# - Ex.: Ana Maria de Souza
# - Primeiro = Ana
# - Último = Souza
print()
print('='*35)
print('Mostre o Primeiro e Último Nome')
print('='*35)
print()
nome = str(input('Entre com seu Nome Completo: ')).strip().split()
print()
print('Seu primeiro nome é: {}'.format(nome[0]))
print('Seu ultimo nome é: {}'.format(nome[len(nome) - 1]))
print()


