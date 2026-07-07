# Desafio 40: Escreva um programa que calcule a media de um aluno (reprovado 5 ou menos; entre 5 e 6.9 recuperacao; 7 ou mais aprovado)
print()
print('-=-'*12)
print('Analizando se Aluno foi Aprovado!')
print('-=-'*12)
print()

nota1 = float(input('Entre com a nota da AV 1: '))
nota2 = float(input('Entre com a nota da AV 2: '))
media = (nota1+nota2)/2

if media <= 5.00:
    print('\nAluno Reprovado!')
elif media >= 7.00:
    print('\nAluno Aprovado!')
else:
    print('\nAluno em Recuperação!')
print('\nFim do programa...\n')

