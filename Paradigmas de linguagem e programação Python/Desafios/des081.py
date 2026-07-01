#Desafio  081: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
#A) Quantos números foram digitados.
#B) A lista de valores, ordenada de forma decrescente.
#C) Se o valor 5 foi digitado e está ou não na lista.
print('-='*30)
print('{:^60}'.format('DESAFIO 81'))
print('-='*30)
lista = []
cont = 0
op = 'S'
while op in 'Ss':
    valor = int(input('\nDigite um Valor: '))
    lista.append(valor)
    print(f'Valor {valor} Adicionado com sucesso!')
    cont +=1
    op = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if op in 'Nn':
        break
print('-='*30)
print(f'Foram digitados {cont} números.')
lista.sort(reverse=True)
print(f'A lista em Ordem Decrescente {lista}')
if 5 in lista:
    print('Foi encontrado o número 5 na Lista')
else:
    print('Não foi encontrado o número 5 na Lista')
print('-='*30)
print('\nFIM...\n')