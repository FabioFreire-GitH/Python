#Desafio  092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. 
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, 
# além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import date
print('-='*30)
print('{:^60}'.format('DESAFIO 92'))
print('-='*30)
print()
trabalhador = dict()

trabalhador['nome'] = str(input('Digite o seu nome: ')).strip()
anonasc = int(input('Ano de Nascimento: '))
trabalhador['idade'] = date.today().year - anonasc
trabalhador['ctps'] = int(input('Carteira de Trabalho (0 se não tiver): '))
while True:
    if trabalhador['ctps'] != 0:
        trabalhador['contratação'] = int(input('Qual o ano de sua Contratação: '))
        trabalhador['salário'] = float(input('Qual o salário R$: '))
        anostrab = 0
        anostrab = date.today().year - trabalhador['contratação']
        trabalhador['aposentadoria'] = 35 - anostrab + trabalhador['idade']
    break
print()
print('-'*30)
print(f'O trabalhador se chama: {trabalhador["nome"]}.')
print(f'Tem {trabalhador["idade"]} anos de idade.')
print(f'O número da CTPS é: {trabalhador["ctps"]}.')
if trabalhador['ctps'] > 0:
    print(f'Foi contratado em {trabalhador["contratação"]}.')
    print(f'Com salário de R$ {trabalhador["salário"]:.2f}.')
    print(f'Se aposenta com {trabalhador["aposentadoria"]} anos de idade.')
print()
print('\nFim\n')


