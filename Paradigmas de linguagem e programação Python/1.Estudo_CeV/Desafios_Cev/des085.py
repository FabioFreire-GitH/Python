# Desafio085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. 
# No final, mostre os valores pares e ímpares em ordem crescente.
print('-='*30)
print('{:^60}'.format('DESAFIO 85'))
print('-='*30)
total = list()
temp = list()
par = list()
impar = list()

for c in range(0,7):
    temp.append(int(input(f'Digite o {c+1}º número: ')))
    if temp[0] % 2 == 0:
        par.append(temp[:])
    else:
        impar.append(temp[:])
    temp.clear()
par.sort()
impar.sort()
total.append(par[:])
total.append(impar[:])
print(temp)
print(f'Os valores pares digitados foram: {par}')
print(f'Os valores ímpares digitados foram: {impar}')
print(f'\nAqui esta a lista total: {total}')
print('\nFim...\n')
print('-='*30)
print('{:^60}'.format('RESOLUÇÃO GUANABARA'))
print('-='*30)