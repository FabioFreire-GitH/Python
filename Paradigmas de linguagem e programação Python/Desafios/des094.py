#Desafio 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: 
#A) Quantas pessoas foram cadastradas
#B) A média de idade
#C) Uma lista com as mulheres
#D) Uma lista de pessoas com idade acima da média
print()
print('-='*30)
print('{:^60}'.format('DESAFIO 94'))
print('-='*30)
print()
pessoa = dict()#para guardar informacoes de UMA PESSOA
lista = list()#para guardar todas as pessoas
soma = media = 0
while True:
    pessoa['nome'] = str(input('Nome: ')).strip().title()
    pessoa['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
    while pessoa['sexo'] not in 'MmFf':
        pessoa['sexo'] = str(input('Opção Invalida! Sexo [M/F]: ')).strip().upper()[0]
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    lista.append(pessoa.copy())
    pessoa.clear()
    op = str(input('Desaja Continuar? [S/N] ')).strip().upper()[0]
    if op == 'N':
        break
    while op != 'S' and op != 'N':
        op = str(input('Opção Invalida. Deseja Continuar? [S/N] ')).strip().upper()[0]
    print()
print()
print('-='*30)
print(f'Foram cadastradas {len(lista)} pessoas!')
media = soma / len(lista)
print(f'A media de idade é {media:.2f}')
print(f'As mulheres cadastradas foram: ',end='')
for p in lista:
    if p['sexo'] == 'F':
        print(f'[{p["nome"]}] ', end='')
print(f'\nAs pessoas com idade acima da media foram: ',end='')
for p in lista:
    if p['idade'] > media:
        print(f'[{p["nome"]}] ',end='')
print()  
print('-='*30)
print('\nFim...\n')
