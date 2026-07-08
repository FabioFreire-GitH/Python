'''
Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''

from msvcrt import getch

print()
print('-=-'*10)
print('Operações Matemáticas')
print('-=-'*10)

num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo  número: '))
opcao = resultado = 0
while opcao != 5:
    print('''
------- OPÇÕES -------
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
----------------------''')
    opcao = int(input('Escolha a operação Matemática: '))
    if opcao == 1:
        resultado = num1 + num2
        print('\nA soma entre {} + {} é igual a {}.'.format(num1,num2,resultado))
        print('\nPressione qualquer tecla para continuar...')
        getch()
    elif opcao == 2:
        resultado = num1 * num2
        print('\nO produto entre {} x {} é igual a {}.'.format(num1,num2,resultado))
        print('\nPressione qualquer tecla para continuar...')
        getch()
    elif opcao == 3:
        if num1 > num2:
            print('\nO número {} é maior que {}.'.format(num1,num2))
            print('\nPressione qualquer tecla para continuar...')
            getch()
        elif num2 > num1:
            print('\nO número {} é maior que {}.'.format(num2,num1))
            print('\nPressione qualquer tecla para continuar...')
            getch()
        else:
            print('\nNumeros {} e {} São Iguais!!!'. format(num1,num2))
            print('\nPressione qualquer tecla para continuar...')
            getch()
    elif opcao == 4:
        num1 = int(input('\nPrimeiro número: '))
        num2 = int(input('Segundo  número: '))
        print('\nPressione qualquer tecla para continuar...')
        getch()
print('\nSaindo do Programa...\n')


