# Desafio 45: Escreva um programa que faça o computador jogar jokenpo com você.
from random import randint
from time import sleep
print()
print('-='*15)
print('Jokempô')
print('-='*15)
itens = ('Pedra','Papel','Tesoura')
computador = randint(0, 2)
print('''Suas opções: 
    [ 1 ] Pedra
    [ 2 ] Papel
    [ 3 ] Tesoura ''')
jogador = int(input('Qual sua jogada? ')) - 1
print('-='*15)
print('O computador escolheu {}!'.format(itens[computador]))
print('O Jogador escolheu {}!'.format(itens[jogador]))
print('-='*15)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')

if computador == 0: #computador jogou PEDRA
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('JOGADOR VENCE!')
    elif jogador == 2:
        print('COMPUTADOR VENCE!')
    else:
        print('JOGADA INVALIDA!')
elif computador == 1: #computador jogou PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCE!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('JOGADOR VENCE!')
    else:
        print('JOGADA INVALIDA!')
elif computador == 2: # computador jogou TESOURA
    if jogador == 0:
        print('JOGADOR VENCE!')
    elif jogador == 1:
        print('COMPUTADOR VENCE!')
    elif jogador == 2:
        print('EMPATE!')
    else:
        print('JOGADA INVALIDA!')
print('-='*15)        


