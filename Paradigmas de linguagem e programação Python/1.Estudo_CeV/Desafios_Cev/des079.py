#Desafio 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. 
#No final, serão exibidos todos os valores únicos digitados, em ordem crescente. 
numlista = list()
op = 'S'
while op in 'Ss':
    valor = (int(input('\nDigite um valor: ')))
    if valor in numlista:
        print('Valor ja existe. Não vou adicionar.')
    else:
        numlista.append(valor)
        print('Valor Adicionado!')
    op = str(input('Deseja Continuar? [S/N] ')).strip().upper()[0]
    if op != 'S' and op != 'N':
        print('Digite apenas S ou N.')
    if op == 'N':
        break
numlista.sort()
print()
print(numlista)
print('\nFim\n')
