# Desafio 38: Escreva um programa que leia dois numeros e compare retorne qual o maior ou são iguais
print()
print('='*30)
print('Verificar Maior número')
print('='*30)
print()
a = int(input('Primeiro número: '))
b = int(input('Segundo número: '))

if a>b:
    print('O valor {} é maior que o valor {}'.format(a,b))
elif b>a:
    print('O valor {} é maior que o valor {}'.format(b,a))
else:
    print('Os valores {} e {} são iguais.'.format(a,b))
print('\nFim...\n')
