#Desafio 34 - Escreva um programa que leia o salario e calcule o valor do seu aumento.
#para salarios superiores a R$ 1.250,00, calcule um aumento de 10%.
#para os inferiores ou iguais, o aumento é de 15%.
print()
print('='*30)
print('Aumento de Salário')
print('='*30)
print()

salario = float(input('Digite o salário: '))
if salario > 1250.00:
    print('Você teve um aumento de 10% = {:.2f}'.format(salario*10/100))
    salario = salario + salario * 10 / 100
else:
    print('Você teve um aumento de 15% = {:.2f}'.format(salario*15/100))
    salario = salario + salario * 15 / 100
print('\nO seu novo salario é: R$ {:.2f}'.format(salario))
print()

