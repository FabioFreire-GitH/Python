#Desafio 071: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas 
# de cada valor serão entregues. 
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
print()
print('-='*20)
print('{:^40}'.format('Caixa Eletrônico'))
print('-='*20)

saque = int(input('Qual o valor do saque? R$ '))
print()
rest = saque
ced = 50
contced = 0

while True:
    if rest >= ced:
        rest -= ced
        contced += 1
    else:
        if contced > 0:
            print(f'Total de {contced} cédulas de R$ {ced:.2f}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        contced = 0
        if rest == 0:
            break
print('-='*20)
print(f'\nSaque de RS{saque} efetuado. Volte sempre!\n')
    
    
