# Desafio 82: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, 
#respectivamente. Ao final, mostre o conteúdo das três listas geradas.
print('-='*30)
print('{:^60}'.format('DESAFIO 82'))
print('-='*30)
valores = []
par = [] 
impar = []
while True:
    valor = int(input('Digite um valor: '))
    valores.append(valor)
    if valor % 2 == 0:
        par.append(valor)
    else:
        impar.append(valor)
    op = str(input('Deseja Continuar? [S/N] ')).strip().upper()[0]
    if op in 'Nn':
        break
print()
print('-='*30)
print(f'Lista Original digitada {valores}')
print(f'Lista de Valores Pares {par}')
print(f'Lista de Valores Impares {impar}')
print('-='*30)