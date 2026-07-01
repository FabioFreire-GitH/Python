#Desafio 25 - Escreva um programa que leia o de uma pessoa e verifique se tem "SILVA" no nome.
print()
print('='*30)
print('Verifica Silva')
print('='*30)
print()
nome = str(input('Qual seu nome completo? ')).strip().upper()
print('\n Verificando se existe Silva em seu nome... {}'. format('SILVA' in nome)) # o in nao é im metodo é um operador
print()
