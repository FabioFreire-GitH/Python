#Desafio  095: Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
jogador = dict()
partidas = list()#para guardar os gols
time = list()
print('-='*30)
print('{:^60}'.format('DESAFIO 95'))
print('-='*30)

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do Jogador: ')).strip().title()
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for c in range(0, tot):
        partidas.append(int(input(f'  ==> Quantos gols na partida {c+1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    partidas.clear()
    while True: #diferente do que eu fiz no des94 - esse foi o guanabara - incluido aqui para estudo e nova perspectiva!
        op = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        if op in 'SN':
            break
        print('Opção Invalida!')
    print()
    if op == 'N':
        break
print('-'*40)
print('Cod ', end ='')
for i in jogador.keys():
    print(f'{i:<15} ', end='')
print()
print('-'*40)
for i, v in enumerate(time):
    print(f'{i+1:<4}', end='')
    for d in v.values():
        print(f'{str(d):<16}',end='')
    print()
print('-'*40)
while True:
    detalhar = int(input('Mostrar Jogador? Digite o Cod: [999 SAIR] '))
    if detalhar == 999:
        break
    if detalhar  > len(time):
        print(f'Não existe ojogador com Cod {detalhar}')
    else:
        print(f'\n LEVANTAMENTO DO JOGADOR: {time[detalhar-1]["nome"]}')
        for i, g in enumerate(time[detalhar-1]['gols']):
            print(f' => No jogo {i+1} fez {g} gols')
    print('-'*40)
print('\nFim...\n')
