#Desafio  068: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que
# ele conquistou no final do jogo. 
from random import randint
print()
print('-=-'*7)
print('PAR OU IMPAR')
print('-=-'*7)
op = '' #opcao jogador 
vit = res = 0 #vitorias e resultado
while vit >= 0:
    print('''
    --- OPÇÕES   ---
    [ P ] PAR
    [ I ] IMPAR
    ''')
    op = str(input('Escola a Opção: ')).strip().upper()[0]
    if op != 'P' and op != 'I':
        print('\nOpção invalida!!')
    else:
        nj = int(input('\nDiga o valor: '))
        nc = randint(0,10)
        print(f'\nVocê jogou {nj} e o computador {nc}. Total {nc+nj}', end = ' ')
        res = (nj+nc)%2
        if op in 'Pp' and res == 0:
            print('deu PAR.\n\nVocê VENCEU!!!')
            vit += 1
        elif op in 'Ii' and res != 0:
            print('deu IMPAR.\n\nVocê VENCEU!!!')
            vit += 1
        else:
            if res == 0:
                print('deu PAR.\n\nVocê PERDEU!!!')
                break
            else:
                print('deu IMPAR.\n\nVocê PERDEU!!!')
                break
print (f'\nVocê venceu {vit} partidas seguidas.\n\n Fim de Programa...\n')





