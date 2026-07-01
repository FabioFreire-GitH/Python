# Desafio 37: Escreva um programa que leia um numero inteiro e peç para o usuario escolher a base de conversão:
# - 1 para binario
# - 2 para octal
# - 3 para hexadecimal
print()
print('='*30)
print('Conversão de Base')
print('='*30)
print()

n = int(input('Digite um número inteiro: '))
print('''\nEscolha um opção abaixo:
(1) - Converter em BINÁRIO
(2) - Converter em OCTAL
(3) - Converter em HEXADECIMAL''')
print()
opcao = int(input('Escolha a uma das opções acima: '))
if opcao == 1:
    print ('\nConversão em Binario: {}'.format(bin(n)[2:]))
elif opcao == 2:
    print ('\nConversão em Octal: {}'.format(oct(n)[2:]))
elif opcao == 3:
    print('\nConversão em Hexadecimal: {}'.format(hex(n)[2:]))
else:
     print('\nOpção Inválida!')
print('\nFim...\n')



