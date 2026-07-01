# Desafio 058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
from random import randint
print()
print('-=-'*10)
print('Adivinhe o Número 2.0')
print('-=-'*10)
print()

comp = randint(1,10)
palpites = 1
print('Tente advinhar o número escolhido pelo Computador!')
usu = int(input('\nDigite um número de 1 a 10: '))
while usu <= 0 or usu > 10:
    usu = int(input('\nNúmero Invalido. Por favor, digite um número de 1 a 10: '))
while usu != comp:
    usu = int(input('\nPalpite Errado!!! Tente novamente: '))
    palpites += 1
print('\nVocê acertou com {} palpites!!!'.format(palpites))
print('\nFim de programa...\n')


