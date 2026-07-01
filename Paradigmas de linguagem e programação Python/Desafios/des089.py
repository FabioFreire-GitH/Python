#Desafio  089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e 
# permita que o usuário possa mostrar as notas de cada aluno individualmente.
alunos = list()
temp = list()
print('-='*30)
print('{:^60}'.format('DESAFIO 89'))
print('-='*30)
print()
print('-'*30)
print('Cadastro de Alunos e suas Notas:')
print('-'*30)
while True:
    temp.append(str(input('\nNome do Aluno: ')).strip())
    temp.append(float(input('Nota 1: ')))
    temp.append(float(input('Nota 2: ')))
    alunos.append(temp[:])
    temp.clear()
    op = str(input('Deseja Continuar? [S/N] ')).strip().upper()[0]
    if op == 'N':
        break
    while op != 'S' and op != 'N':
        op = str(input('Opção Invalida. Deseja Continuar? [S/N] ')).strip().upper()[0]
print()
print('-'*30)
print('{:<3} {:<20} {:>5}'.format('No.','NOME','MÉDIA'))
print('-'*30)
for i, a in enumerate(alunos):
    print(f'{i+1:<3} {a[0]:<20} {(a[1]+a[2])/2:>5.2f}')
print('-'*30)
while True:
    op2 = int(input('Digite o No. do Aluno para ver Notas (999 para SAIR): '))
    if op2 == 999:
        break
    for i, a in enumerate(alunos):
        if op2 -1 == i:
            print(f'As notas de {a[0]} são [{a[1]:.2f}, {a[2]:.2f}].')
            print('-'*30)
print('\nFIM\n')

