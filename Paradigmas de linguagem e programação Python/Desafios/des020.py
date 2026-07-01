#Desafio 20 - O mesmo professor do desafio anterior quer sortear a ordem de apresentaçao de trabalhos dos alunos. 
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
print()
print('='*30)
print('Sorteio ordem de Aluno')
print('='*30)
print()
aluno = ['','','','']
aluno[0] = str(input('Entre com o primeiro Aluno: '))
aluno[1] = str(input('Entre com o segundo Aluno: '))
aluno[2] = str(input('Entre com o terceiro Aluno: '))
aluno[3] = str(input('Enrte com o quarto Aluno: '))
print()
import random
random.shuffle(aluno)
print('Ordem de apresentação:')
print()
print('1º - {}'.format(aluno[0]))
print('2º - {}'.format(aluno[1]))
print('3º - {}'.format(aluno[2]))
print('4º - {}'.format(aluno[3]))
print()
