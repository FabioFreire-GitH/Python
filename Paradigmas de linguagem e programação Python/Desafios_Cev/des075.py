#Desafio  075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares.+
print()
num = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite o último número: ')))
print(f'\nVocê digitou: {num}')
print(f'\nO valor 9 apareceu {num.count(9)} vezes.')
if 3 in num:
    print(f'O valor 3 foi digitado na(s) posição(ões) {num.index(3)+1}.')
else:
    print('O valor 3 não foi encontrado!')
print(f'Números pares encontrados:',end = '')
for n in num:
    if n % 2 == 0:
        print(f' {n} ', end='')
print('\n')
