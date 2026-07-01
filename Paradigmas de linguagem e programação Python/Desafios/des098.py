#Desafio 098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:
#a) de 1 até 10, de 1 em 1
#b) de 10 até 0, de 2 em 2
#c) uma contagem personalizada

from time import sleep
def contagem(i, f, p):
    if p == 0:
        p = 1
    if i > f and p > 0:
        p = p*-1
    if i < f and p < 0:
        p = p*-1
    print('-='*30)
    print(f'Contagem de {i} a {f} de {p} em {p}. ')
    for c in range(i, f+p, p):
        print(f'{c} ', end ='', flush=True)
        sleep(0.5)
    print('Fim!')
    print('-='*30)


print()
contagem(1, 10, 1)
contagem(10, 0, -2)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Inicio: '))
fim = int(input('Fim: '))
raz = int(input('Passo: '))
contagem(ini, fim, raz)
print()
print('Saindo...\n')