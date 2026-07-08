#Desafio 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista. 
print()
listanum = list()
for c in range(0, 5):
    valor = input(f'Digite um numero na posição {c}: ')
    if valor == '':
        print('Campo Vazio!')
    else:
        listanum.append(int(valor))
print(f'\nOs valores incluidos na LISTA são {listanum}')
print(f'\nO maior valor é o {max(listanum)} nas posições ', end ='')
for i, v in enumerate(listanum):
    if v == max(listanum):
        print(f'{i} ', end='')
print(f'\nO menor valor é o {min(listanum)} nas posições ', end ='')
for i, v in enumerate(listanum):
    if v == min(listanum):
        print(f'{i} ', end='')
print('\n\nFim...\n')
