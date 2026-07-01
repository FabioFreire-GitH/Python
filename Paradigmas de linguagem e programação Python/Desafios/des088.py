#Desafio 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, 
# cadastrando tudo em uma lista composta.

from random import randint
from time import sleep
jogo = list()
jogos = list()
print('-='*30)
print('{:^60}'.format('DESAFIO 88'))
print('-='*30)
qtd = int(input('\nQuantos jogos quer que eu sorteie? '))
tot = 1
while tot <= qtd:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in jogo:
            jogo.append(num)
            cont += 1
        if cont >= 6:
            break
    jogo.sort()
    jogos.append(jogo[:])
    jogo.clear()
    tot += 1
print()
print('-='*3, f'SORTEANDO {qtd} JOGOS', '-='*3)
for i, j in enumerate(jogos):
    sleep(1)
    print(f'Jogo {i}: {j}')
sleep(1)
print('-='*3, '{:^17}'.format('FIM DO SORTEIO'), '-='*3)
print()








