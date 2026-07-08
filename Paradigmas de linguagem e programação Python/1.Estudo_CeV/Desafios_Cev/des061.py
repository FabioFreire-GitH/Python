# Desafio 061 : Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
print()
print('-=-'*8)
print('Progressão Aritmética 2.0 (While)')
print('-=-'*8)
print()
primeiro = int(input('Entre com o primeiro Termo: '))
razao = int(input('Entre com a razão: '))
pos = int(input('Entre com a Posição desejada: '))
termo = primeiro
cont = 1
print('PA = (', end =' ')
while cont <= pos:
    print('{}'.format(termo), end = ' -> ')
    termo += razao
    cont += 1
print('Fim )')
print('\nSaindo do programa...\n')
    