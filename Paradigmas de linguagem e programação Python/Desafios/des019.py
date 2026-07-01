#Desafio 19 - Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
print()
print('='*30)
print('Sorteio de Aluno')
print('='*30)
print()
aluno = ['','','','']
aluno[0] = str(input('Entre com o primeiro Aluno: '))
aluno[1] = str(input('Entre com o segundo Aluno: '))
aluno[2] = str(input('Entre com o terceiro Aluno: '))
aluno[3] = str(input('Enrte com o quarto Aluno: '))
print()
import random
sorteio = random.randint(1,4)
print('O aluno sorteado foi: {}'. format(aluno[sorteio - 1]))
print()

# Outra Forma mais SIMPLES
# import random
# n1 = str(input('Nome :'))
# n2 = str(input('Nome :'))
# n3 = str(input('Nome :'))
# n4 = str(input('Nome :'))
# lista = [n1, n2, n3, n4]
# escolha = random.choice(lista) 
# print('O escolhido foi {}'.format(escolha))



