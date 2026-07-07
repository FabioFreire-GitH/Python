#Desafio  093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de 
#gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
jogador = dict()
partidas = list()#para guardar os gols
print('-='*30)
print('{:^60}'.format('DESAFIO 93'))
print('-='*30)
jogador['nome'] = str(input('Nome do Jogador: ')).strip()
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0, tot):
    partidas.append(int(input(f'  ==> Quantos gols na partida {c+1}? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-='*30)
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f'O campo [{k}] tem o valor [{v}]')
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')# tot tambem funcionaria neste caso
for i, v in enumerate(jogador['gols']):
    print(f'  ==> Na partida {i+1} converteu {v} gols.')
print('-='*30)
print('\nFim...\n')

#Aqui tem lista dentro de dicinario