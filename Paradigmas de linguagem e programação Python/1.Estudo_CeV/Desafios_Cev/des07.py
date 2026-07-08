#Desafio 7 - Desenvolva um programa que leia a duas notas de uma aluno, calcule e mostre a sua media.
print()
print('='*30)
print('Calculo da Media de um Aluno')
print('='*30)
nome = input('Entre com o nome do aluno: ')
nota1 = float(input('\nEntre com a primeira Nota: '))
nota2 = float(input('Entre com a segunda Nota: '))
media = (nota1+nota2)/2
print('\nA média do aluno {}, é {}!'.format(nome, media))
print()
