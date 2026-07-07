#Desafio 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
print('-='*30)
print('{:^60}'.format('DESAFIO 90'))
print('-='*30)
aluno = {}
aluno['nome'] = str(input('Nome do Aluno: ')).strip()
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
print(f'A média de {aluno["nome"]} é {aluno["media"]:.2f}')
if aluno['media'] >= 7.00:
    aluno['situacao'] = 'Aprovado'
else:
    aluno['situacao'] = 'Reprovado'
print(f'Situação: {aluno["situacao"]}')

print(f'\nExibindo o conteudo do dicionario: {aluno}')
print('\nFim\n')
