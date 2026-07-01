#Desafio 103: Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar 
# a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
def ficha(n, g):
    if n == '':
        n = '<desconhecido>'
    if g == '':
        g = 0
    return print(f'O jogador {n} fez {g} gols no campeonato.')


print()
print('-'*30)
print('{:^30}'.format('GOLS MARCADOS'))
print('-'*30)
nome = str(input('Nome do Jogador: ')).strip()
gols = input('Número de Gols: ')
ficha(nome, gols)