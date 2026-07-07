#Desafio 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. 
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
from time import sleep
from random import randint
from operator import itemgetter
print('-='*30)
print('{:^60}'.format('DESAFIO 91'))
print('-='*30)
print()
jogada = dict()
resultado = list()
print(f'-'*3 , 'SORTEIO DOS DADOS',  '-'*3)
for c in range(0,4):
    dado = randint(1, 6)
    sleep(1)
    print(f'O jogador {c+1} tirou {dado} no dado.')
    jogada['jogador'+str(c+1)] = dado
resultado = sorted(jogada.items(), key=itemgetter(1), reverse=True)
print()
sleep(1)
print(f'-'*3 , 'RANKING VENCEDOR',  '-'*3)
for i, v in enumerate(resultado):
    print(f'O {i+1}º Lugar foi: {v[0]} com {v[1]} no dado.')
print()
