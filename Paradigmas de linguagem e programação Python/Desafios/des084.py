#Desafio  084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
#A) Quantas pessoas foram cadastradas.
#B) Uma listagem com as pessoas mais pesadas.
#C) Uma listagem com as pessoas mais leves.
print('-='*30)
print('{:^60}'.format('DESAFIO 84'))
print('-='*30)
pessoas = list()
dado = list()
maior = menor = 0
while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso (Kg): ')))
    if len(pessoas) == 0:
        maior = menor = dado[1]
    else:
        if dado[1] > maior:
            maior = dado[1]
        if dado[1] < menor:
            menor = dado[1]
    pessoas.append(dado[:])
    dado.clear()
    op = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    print()
    if op == 'N':
        break
print(f'Foram cadastradas {len(pessoas)} pessoas.')  
print(f'O Maior peso foi de {maior:.2f}Kg: ', end='') 
for p in pessoas:
        if p[1] == maior:
             print(f'[{p[0]}] ', end='')
print(f'\nO Menor peso foi de {menor:.2f}Kg: ', end='')                 
for p in pessoas:
        if p[1] == menor:
             print(f'[{p[0]}] ', end='')
print('\n\nFim...\n')     

